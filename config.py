import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir,'.env'))


# os.environ['DATABASE_URL'] = "mysql+pymysql://root:ASDFGHJKL@127.0.0.1/MicroBlog"

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
                              'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # MAIL_SERVER = os.environ.get('MAIL_SERVER')
    # MAIL_PORT = int(os.environ.get('MAIL_PORT') or 25)
    # MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') is not None
    # MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    # MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    ADMINS = ['17764563720@163.com']
    POSTS_PER_PAGE = 3  # 每页配置数

    MAIL_SERVER = 'smtp.163.com'
    MAIL_PORT = 25
    MAIL_USERNAME = '17764563720@163.com'
    MAIL_PASSWORD = 'JNNAAHRYUXAPCQYV'  # 163邮箱授权码


    LANGUAGES = ['en','es']  #支持语言列表
    ELASTICSEARCH_URL = os.environ.get('ELASTICSEARCH_URL')


# print(os.path.join(basedir, 'ooo.py'))


