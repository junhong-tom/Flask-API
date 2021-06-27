from flask import Flask
from flask import render_template
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from config import Config
import os

#  目標: Flask SQLAlchemy 的用法
#  https://flask-sqlalchemy.palletsprojects.com/en/2.x/quickstart/
#  安裝 flask-sqlalchemy


app = Flask(__name__)
bootstrap = Bootstrap(app)

db = SQLAlchemy(app)
app.config.from_object(Config)
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