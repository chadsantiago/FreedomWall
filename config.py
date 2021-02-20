import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class Production(Config):
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')

class Development(Config):
    DEBUG = False
    ENV = 'development'
    DEVELOPMENT = False
    SECRET_KEY = 'KPa6lCS&b2e@JW4!?s'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///stories.db'