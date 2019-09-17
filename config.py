import os

class Config:
    SOURCES_API_BASE_URL = 'https://newsapi.org/v2/sources?category={}&apiKey={}'
    ARTICLES_BASE_URL = 'https://newsapi.org/v2/everything?sources={}&apiKey={}'
    SOURCE_API_KEY = '162ff051a21c4eb1a7bd52346af6a67b'
    SECRET_KEY = os.environ.get('SECRET_KEY')
    print(SOURCE_API_KEY)

class ProdConfig(Config):
    pass


class DevConfig(Config):
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}    