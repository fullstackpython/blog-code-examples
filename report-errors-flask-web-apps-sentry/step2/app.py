# app.py
import os
import sentry_sdk
from flask import Flask, escape, request
from sentry_sdk.integrations.flask import FlaskIntegration


sentry_sdk.init(
    dsn="https://{}.ingest.sentry.io/{}".format(os.getenv('SENTRY_KEY'),
                                                os.getenv('SENTRY_APP_ID')),
    integrations=[FlaskIntegration()]
)


app = Flask(__name__)


@app.route('/divide/<int:numerator>/by/<int:denominator>/')
def hello(numerator, denominator):
    answer = numerator / denominator
    return f'{numerator} can be divided by {denominator} {answer} times.'
