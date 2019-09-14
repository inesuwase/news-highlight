import os

class Config:

    NEWS_API_BASE_URL =https://newsapi.org/v2/everything?q=bitcoin&from=2019-08-12&sortBy=publishedAt&api_key={}'
    NEWS_API_KEY = os.environ.get('News_API_KEY')
    SECRET_KEY = os.environ.get('SECRET_KEY')


class ProdConfig(Config):
    pass


class DevConfig(Config):
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}