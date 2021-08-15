import os

base_dir = os.path.abspath(os.getcwd())


# base config class
class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv('secret_key') or os.urandom(24)


class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{base_dir}/devdb.sqlite3"
    DEBUG = True

class TestingConfig(Config):
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{base_dir}/testdb.sqlite3"
    DEBUG = True

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABSE_URL') # heroku sets this envvar by default
    # we'll add more things here later on

config_ = {
    'default': DevelopmentConfig,
    'development': DevelopmentConfig,
    'production': ProductionConfig
}