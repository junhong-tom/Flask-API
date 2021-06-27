from flask import Flask
from flask import render_template
import os

# 目標: 模板的繼承
# 1.  基礎模板  base.html
# 2.  extends 的使用
# 3.  模板的引用 nabvar.html
# 4.  include 的使用

app = Flask(__name__)

@app.route('/')
def index():
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