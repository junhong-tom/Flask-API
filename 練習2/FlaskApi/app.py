from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "hello,flask"

if __name__ == '__main__':
    app.run(debug=True) #  debug=True, 可以立即顯示編輯後的內容