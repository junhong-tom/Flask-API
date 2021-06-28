import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    # database configuration

    # SECRET KEY
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'A-VERY-LONG-SECRET-KEY'

    # Google reCAPTCHA 驗證 可以使用 FAQ 文件 所提供的 test key 跳過申請步驟
    # https://medium.com/pyladies-taiwan/flask-wtf-%E8%A1%A8%E5%96%AE%E9%A9%97%E8%AD%89-4b4423eeeb45
    RECAPTCHA_PUBLIC_KEY = '6LeIxAcTAAAAAJcZVRqyHh71UMIEGNQ_MXjiZKhI'
    RECAPTCHA_PRIVATE_KEY = '6LeIxAcTAAAAAGG-vFI1TnRWxMZNFuojJ4WifJWe'


    # 先從環境變量獲取 Database 的 URL ，如果沒有則從本地創建一個 app.db
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' +os.path.join(basedir, 'app.db')

    SQLALCHEMY_TRACK_MODIFICATIONS = False