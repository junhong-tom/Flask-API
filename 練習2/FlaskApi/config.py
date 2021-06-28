import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    # database configuration

    # SECRET KEY
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'A-VERY-LONG-SECRET-KEY'

    # 先從環境變量獲取 Database 的 URL ，如果沒有則從本地創建一個 app.db
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' +os.path.join(basedir,'app.db')

    SQLALCHEMY_TRACK_MODIFICATIONS = False