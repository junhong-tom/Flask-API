from flask import Flask

# use render_template
# Check template file
from flask import render_template
import os
app = Flask(__name__)



@app.route('/')
def index():
    return "hello,flask"


# return html 語言
@app.route('/html')
def hmtlindex():
    return "<h1>hello,flask</h1>"

# 抽取 HTML
@app.route('/render_template')
def index_template():
    # 傳參數給 template
    #title = 'Flask Web App'
    paragraphs =[
        'section1',
        'section2',
        'section3'
    ]
    return render_template('index.html',title='Home',data=paragraphs)

if __name__ == '__main__':
    app.run(debug=True) #  debug=True, 可以立即顯示編輯後的內容