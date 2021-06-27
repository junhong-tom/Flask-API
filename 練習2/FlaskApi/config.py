import os
basedir = os.path.abspath(os.path.basename(__file__))
print(basedir)
class Config(object):
    # database configuration
    # 先從環境變量獲取 Database 的 URL ，如果沒有則從本地創建一個 app.db
    # 路徑錯: 'sqlite:///' +os.path.join(basedir,'app.db') 事後再來除錯
    #SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' +os.path.join(basedir,'app.db')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or r'sqlite:///C:/Users/Tom/PycharmProjects/FlaskApi/app.db'


    SQLALCHEMY_TRACK_MODIFICATIONS = False