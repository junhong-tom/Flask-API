from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from config import Config
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

#from models import User

#  目標: Flask loging (表單) 的用法
#  https://flask-login.readthedocs.io/en/latest/
#  安裝 flask-login



app = Flask(__name__)
app.config.from_object(Config)
bootstrap = Bootstrap(app)
bcrypt = Bcrypt(app)
db = SQLAlchemy(app)
login = LoginManager(app)
login.login_view = 'login'
login.login_message = 'You must login to access this page'
login.login_message_category = 'info'


from app.routing import *