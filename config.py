
import os
from dotenv import load_dotenv,find_dotenv

load_dotenv(find_dotenv())

class Config:
    SQLAlchemy_DATABASE_URI=os.getenv('SQLAlchemy_DATABASE_URL')
    DEBUG=os.getenv('DEBUG')

class ProdConfig(Config):
    DEBUG = False

class DevConfig(Config):
   DEBUG = True


config_options={
    'development':DevConfig,
    'production':ProdConfig
}