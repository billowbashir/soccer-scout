class Config:

    '''
    class config
    '''
    SECRET_KEY='1234'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://bashir:bashiir@localhost/soccer_scout'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    UPLOADED_PHOTOS_DEST ='app/static/photos'

class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''


class TestConfig(Config):
    '''
    test configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
    '''

class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True

config_options = {
'development':DevConfig,
'test':TestConfig,
'production':ProdConfig
}
