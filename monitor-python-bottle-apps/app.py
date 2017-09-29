import bottle
import os
import re
from bottle import route, template
from rollbar.contrib.bottle import RollbarBottleReporter


TEMPLATE_STRING = """
<html>
 <head>
  <title>Full Stack Python Web App</title>
 </head>
 <body>
  <h1>{{ h1 }}</h1>
 </body>
</html>
"""

MIN_MSG_LENGTH = 2
ROLLBAR_SECRET = os.environ.get("ROLLBAR_SECRET")

rb_monitor = RollbarBottleReporter(access_token=ROLLBAR_SECRET,
                                   environment='production')
bottle.install(rb_monitor)


@route("/<msg>/")
def show_message(msg):
    """Display a message if the msg value is greater than 2 characters
    in the path.
    """
    valid_length = len(msg) >= MIN_MSG_LENGTH
    valid_name = re.match('^[a-z\-]+$', msg.lower()) is not None
    if valid_length and valid_name:
        return template(TEMPLATE_STRING, h1=msg)
    else:
        error_msg = "Sorry, only alpha characters and hyphens allowed."
        raise Exception(error_msg)


if __name__ == "__main__":
    bottle.run(host='localhost', port=8080)
