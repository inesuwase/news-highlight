import os

class Config:

    NEWS_API_BASE_URL =https://newsapi.org/v2/everything?q=bitcoin&from=2019-08-12&sortBy=publishedAt&apiKey=162ff051a21c4eb1a7bd52346af6a67b'
    NEWS_API_KEY = os.environ.get('NEWS_API_KEY')
    SECRET_KEY = os.environ.get('SECRET_KEY')


class ProdConfig(Config):
    pass


class DevConfig(Config):
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}