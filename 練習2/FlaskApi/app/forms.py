from flask_wtf import FlaskForm
from flask_wtf.recaptcha import RecaptchaField
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import  DataRequired, Length, Email,EqualTo, ValidationError

from app.models import User


#  如果遇到這樣的狀況: Exception: Install 'email_validator' for email validation support.
#  解決方法: 需要 Install 套件  email_validator

#  如果遇到這樣的狀況: RuntimeError: A secret key is required to use CSRF.
#  解決方法: configure 設定

#  如果遇到這樣的狀況: RuntimeError: RECAPTCHA_PUBLIC_KEY config not set
#  解決方法: configure 設定

class RegisterForm(FlaskForm):
    # 因 db 的欄位屬性: unique，導致有第二個相同的 username 會報錯
    # sqlalchemy.exc.IntegrityError
    username = StringField('Username',validators=[DataRequired(),Length(min=3,max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=3, max=20)])
    confirm = PasswordField('Repeat Password', validators=[DataRequired(), EqualTo('password')])
    recaptcha = RecaptchaField()
    submit = SubmitField('Register')

    # 錯誤檢查
    def validate_username(self,username):
        check_result = User.query.filter_by(username=username.data).first()
        if check_result:
            raise ValidationError("username already token")

    def validate_email(self, email):
        check_result = User.query.filter_by(email=email.data).first()
        if check_result:
            raise ValidationError("Email already token")
    pass
