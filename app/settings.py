class Default(object):
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:hjy123123@localhost/wop?charset=utf8'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SECRET_KEY= 'asd;dasdacadsa'
    


class Development(Default):
    ENV = 'development'
    DEBUG = True

class Production(Default):
    ENV = 'production'
    DEBUG = False