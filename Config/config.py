import random, string

# ================================
#       default config
# ================================
class BaseConfig(object):
    DEBUG = False
    SECRET_KEY = ''.join(random.choice(string.ascii_uppercase + string.digits) for x in range(32))
    DB_HOST = 'localhost:3306'
    DB_NAME = 'db_base'
    DB_USERNAME = 'root'
    DB_PASSWORD = 'secretPassword'
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://%s:%s@%s/%s" % (DB_USERNAME, DB_PASSWORD, DB_HOST, DB_NAME)
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    CSRF_ENABLED = True
    # Flask-Mail settings
    MAIL_SERVER = ''
    MAIL_PORT = 465
    MAIL_USE_SSL = True
    MAIL_USE_TLS = False
    MAIL_USERNAME = ''
    MAIL_PASSWORD = ''
    MAIL_DEFAULT_SENDER = ''





# ================================
#       development config
# ================================
class DevelopmentConfig(BaseConfig):
    DEBUG = True




class TestConfig(BaseConfig):
    DEBUG = True
    TESTING = True
    WTF_CSRF_ENABLED = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'



class ProductionConfig(BaseConfig):
    DEBUG = False




