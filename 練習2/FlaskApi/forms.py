from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import  DataRequired, Length, Email,EqualTo
#  如果遇到這樣的狀況: Exception: Install 'email_validator' for email validation support.
#  解決方法: 需要 Install 套件  email_validator

#  如果遇到這樣的狀況: RuntimeError: A secret key is required to use CSRF.
#  解決方法: configure 設定

class RegisterForm(FlaskForm):
    username = StringField('Username',validators=[DataRequired(),Length(min=6,max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=8, max=20)])
    confirm = PasswordField('Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')
    pass
