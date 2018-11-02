import os


class Config(object):
    SECRET_KEY = os.getenv('SECRET_KEY') or 'development key'

    # Redis
    REDIS_SERVER = os.getenv('REDIS_SERVER') or 'localhost'
    REDIS_PORT = os.getenv('REDIS_PORT') or 6379
    REDIS_DB = os.getenv('REDIS_DB') or 1
    REDIS_URL = 'redis://{}:{}'.format(REDIS_SERVER, REDIS_PORT)

    # Celery task queue
    CELERY_BROKER_URL = os.getenv('CELERY_BROKER_URL') or REDIS_URL
    CELERY_RESULT_BACKEND = os.getenv('CELERY_RESULT_BACKEND') or REDIS_URL

    # database settings
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL') or \
      'sqlite:///' + os.path.join(os.path.abspath(os.path.dirname(__file__)),
      'flaskdash.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    OIDC_CLIENT_SECRETS = "openidconnect_secrets.json"
    OIDC_COOKIE_SECURE = False
    OIDC_CALLBACK_ROUTE = "/oidc/callback"
    OIDC_SCOPES = ["openid", "email", "profile"]
    OIDC_ID_TOKEN_COOKIE_NAME = "oidc_token"
