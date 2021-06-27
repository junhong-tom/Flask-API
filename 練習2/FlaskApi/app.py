from flask import Flask
from flask import render_template
from flask_bootstrap import Bootstrap

import os

#  目標: Flask Boostrap 插件的用法
#  https://pythonhosted.org/Flask-Bootstrap/basic-usage.html
#  https://getbootstrap.com/docs/3.3/components/
#  安裝 flask_bootstrap 及 import
#  bootstrap/base.html 原生地base.html 在
#  .\FlaskApi\venv\Lib\site-packages\flask_bootstrap\templates\bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)

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