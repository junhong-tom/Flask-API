from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from config import Config
from flask_bcrypt import Bcrypt

#from models import User

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

from app.routing import *