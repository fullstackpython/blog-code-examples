# app.py
from flask import Flask, escape, request


app = Flask(__name__)


@app.route('/divide/<int:numerator>/by/<int:denominator>/')
def hello(numerator, denominator):
    answer = numerator / denominator
    return f'{numerator} can be divided by {denominator} {answer} times.'
