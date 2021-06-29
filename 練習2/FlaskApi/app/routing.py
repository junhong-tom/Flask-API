from flask import flash
from flask import render_template,request
from app.forms import RegisterForm, LoginForm, PasswordResetRequestForm
from app import db,bcrypt,app
from app.models import User
from flask import redirect, url_for
from flask_login import login_user, login_required, current_user, logout_user

@app.route('/')
@login_required
def index():
    return render_template('index.html')

@app.route('/register', methods=['GET','POST'])
def register():
    if current_user.is_authenticated:
        return redirect( url_for('index'))
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
        return redirect(url_for('login'))
        pass
    return render_template('register.html',form=form)


@app.route('/login',methods=['GET','POST'])
def login():
    if current_user.is_authenticated:
        return redirect( url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        remember = form.remember.data
        # Check if password is match
        user = User.query.filter_by(username=username).first()
        if user and bcrypt.check_password_hash(user.password,password):
            # user exist and password is match
            login_user(user=user,remember=remember)
            flash('Login success',category='infor')
            if request.args.get('next'):
                next_page = request.args.get('next')
                print('next_page  ',next_page)
                return redirect( next_page)
            return redirect( url_for('index'))

        flash('user not exitss or password matched',category='danger')

        pass
    return render_template('login.html',form=form)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect( url_for('login'))

@app.route('/send_password_reset_request',methods=['GET','POST'])
def send_password_reset_request():
    if current_user.is_authenticated:
        return redirect( url_for('index'))
    form = PasswordResetRequestForm()
    email = form.email.data
    return render_template('send_password_reset_request.html', form=form)
