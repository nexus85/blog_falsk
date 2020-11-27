class Configuration(object):
    DEBUG = True
    
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root:12345@192.168.1.188/test1'
