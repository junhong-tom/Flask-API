from flask import flash
from flask import render_template
from app.forms import RegisterForm
from app import db,bcrypt,app
from app.models import User
from flask import redirect, url_for

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
        print(username, email, password)
        user = User(username=username,email=email,password=password)
        db.session.add(user)
        db.session.commit()

        flash('Congrates, registeration success', category='success')
        return redirect(url_for('index'))
        pass
    return render_template('register.html',form=form)
