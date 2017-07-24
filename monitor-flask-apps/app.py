import os
import re
import rollbar
from flask import Flask, render_template
from werkzeug.exceptions import NotFound


app = Flask(__name__)
rollbar.init(os.environ.get('ROLLBAR_SECRET'))
rollbar.report_message('Rollbar is configured correctly')

MIN_PAGE_NAME_LENGTH = 2


@app.route("/<string:page>/")
def show_page(page):
    valid_length = len(page) >= MIN_PAGE_NAME_LENGTH
    valid_name = re.match('^[a-z]+$', page.lower()) is not None
    if valid_length and valid_name:
        return render_template("{}.html".format(page))
    else:
        msg = "Sorry, couldn't find page with name {}".format(page)
        raise NotFound(msg)


if __name__ == "__main__":
    app.run(debug=True)
