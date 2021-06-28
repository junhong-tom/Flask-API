from flask import Flask
from flask import render_template
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from config import Config
from forms import RegisterForm

import os

#  目標: Flask WTForms (表單) 的用法
#  https://flask-wtf.readthedocs.io/en/0.15.x/quickstart/
#  安裝 flask-wtf


app = Flask(__name__)
bootstrap = Bootstrap(app)

db = SQLAlchemy(app)
app.config.from_object(Config)
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['GET','POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        pass
    return render_template('register.html',form=form)

if __name__ == '__main__':
    app.run(debug=True) #  debug=True, 可以立即顯示編輯後的內容