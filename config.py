
import os
from dotenv import load_dotenv,find_dotenv

load_dotenv(find_dotenv())

class Config:
    #  email configurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    # SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:isaac@localhost/pitches'
    DEBUG=os.getenv('DEBUG')

class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:isaac@localhost/pitches'
    pass

class DevConfig(Config):
   SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:isaac@localhost/pitches'
   DEBUG = True


config_options={
    'development':DevConfig,
    'production':ProdConfig
}