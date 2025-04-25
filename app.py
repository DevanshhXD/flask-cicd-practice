from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    return "Deployed with CI/CD like a boss 💪"

@app.route('/time')
def time():
    now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    return f"Server time: {now}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
