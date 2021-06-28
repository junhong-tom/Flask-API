from flask_wtf import FlaskForm
from flask_wtf.recaptcha import RecaptchaField
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import  DataRequired, Length, Email,EqualTo


#  如果遇到這樣的狀況: Exception: Install 'email_validator' for email validation support.
#  解決方法: 需要 Install 套件  email_validator

#  如果遇到這樣的狀況: RuntimeError: A secret key is required to use CSRF.
#  解決方法: configure 設定

#  如果遇到這樣的狀況: RuntimeError: RECAPTCHA_PUBLIC_KEY config not set
#  解決方法: configure 設定

class RegisterForm(FlaskForm):
    username = StringField('Username',validators=[DataRequired(),Length(min=3,max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=3, max=20)])
    confirm = PasswordField('Repeat Password', validators=[DataRequired(), EqualTo('password')])
    recaptcha = RecaptchaField()

    submit = SubmitField('Register')
    pass
