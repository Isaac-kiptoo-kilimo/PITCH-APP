
import os



class Config:
    SQLAlchemy_DATABASE_URI=os.getenv('DATABASE_URL')
    DEBUG=os.getenv('DEBUG')

class ProdConfig(Config):
    DEBUG = False

class DevConfig(Config):
   DEBUG = True


config_options={
    'development':DevConfig,
    'production':ProdConfig
}