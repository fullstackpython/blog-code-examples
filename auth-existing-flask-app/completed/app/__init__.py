import redis
from os import environ
from flask import Flask
from app.utils import make_celery
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_oidc import OpenIDConnect
from okta import UsersClient


app = Flask(__name__, static_url_path='/static')
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db) 

# connect to Redis instance
redis_db = redis.StrictRedis(host=app.config['REDIS_SERVER'],
                             port=app.config['REDIS_PORT'],
                             db=app.config['REDIS_DB'])
celery = make_celery(app)


# instantiate OpenID client to handle user session
oidc = OpenIDConnect(app)
# Okta client will determine if a user has an appropriate account
okta_client = UsersClient(environ.get("OKTA_ORG_URL"),
                          environ.get("OKTA_AUTH_TOKEN"))


from app import routes
