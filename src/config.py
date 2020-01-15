import os
from sqlalchemy.engine.url import URL


class Config:
    SECRET_KEY = 'very_secret_key'
    PG_USER = "antonio"
    PG_PASSWORD = "password"
    PG_HOST = "localhost"
    PG_PORT = 5430
    DB_NAME = "postgres"
    SQLALCHEMY_DATABASE_URI = URL(drivername='postgresql',
                                  username=PG_USER,
                                  password=PG_PASSWORD,
                                  host=PG_HOST,
                                  port=PG_PORT,
                                  database=DB_NAME)
    # f"postgresql://{PG_USER}:{PG_PASSWORD}@{PG_HOST}:{PG_PORT}/{DB_NAME}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # SQLALCHEMY_ECHO = True


class DevConfig(Config):
    pass


class ProductionConfig(Config):
    pass


def run_config():
    env = os.environ.get('ENV')
    if env == 'DEV':
        return DevConfig
    elif env == 'PROD':
        return ProductionConfig
    else:
        return Config
