
import os
from dotenv import load_dotenv,find_dotenv

load_dotenv(find_dotenv())

class Config:
    # SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:isaac@localhost/pitches'
    DEBUG=os.getenv('DEBUG')

class ProdConfig(Config):
    
    pass

class DevConfig(Config):
   SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:isaac@localhost/pitches'
   DEBUG = True


config_options={
    'development':DevConfig,
    'production':ProdConfig
}