import os
import re
import rollbar
import rollbar.contrib.flask
from flask import Flask, render_template, Response
from flask import got_request_exception
from werkzeug.exceptions import NotFound


app = Flask(__name__)
MIN_PAGE_NAME_LENGTH = 2


@app.before_first_request
def add_monitoring():
    rollbar.init(os.environ.get('ROLLBAR_SECRET'))
    ## delete the next line if you dont want this event anymore
    rollbar.report_message('Rollbar is configured correctly')
    got_request_exception.connect(rollbar.contrib.flask.report_exception, app)


@app.route("/<string:page>/")
def show_page(page):
    try:
        valid_length = len(page) >= MIN_PAGE_NAME_LENGTH
        valid_name = re.match('^[a-z]+$', page.lower()) is not None
        if valid_length and valid_name:
            return render_template("{}.html".format(page))
        else:
            msg = "Sorry, couldn't find page with name {}".format(page)
            raise NotFound(msg)
    except:
        rollbar.report_exc_info()
        return Response("404 Not Found")


if __name__ == "__main__":
    app.run(debug=True)
