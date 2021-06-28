from flask import Flask, flash
from flask import render_template
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from config import Config
from forms import RegisterForm
from flask_bcrypt import Bcrypt
from models import User

import os

#  目標: Flask WTForms (表單) 的用法
#  https://flask-wtf.readthedocs.io/en/0.15.x/quickstart/
#  flask-bcrypt 加密數據項
#  安裝 flask-wtf
#  Google reCAPTCHA 驗證


app = Flask(__name__)
bootstrap = Bootstrap(app)
bcrypt = Bcrypt(app)
db = SQLAlchemy(app)
app.config.from_object(Config)
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['GET','POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        # 取得 form 中的欄位資料
        username = form.username.data
        # 敏感數據

        password = bcrypt.generate_password_hash(form.password.data)
        # 確認 密碼是否一致 使用 bcrypt.check_password_hash
        #bcrypt.check_password_hash(password,form.password.data)
        email = form.email.data
        user = User(username=username,email=email,password=password)
        db.session.add(user)
        db.session.commit()
        flash('Congrates, registeration success', category='success')
        pass
    return render_template('register.html',form=form)

if __name__ == '__main__':
    app.run(debug=True) #  debug=True, 可以立即顯示編輯後的內容