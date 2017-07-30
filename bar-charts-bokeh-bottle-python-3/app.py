import os
import bottle
from bottle import route, run, template


app = bottle.default_app()

TEMPLATE_STRING = """
<html>
 <head>
  <title>Bar charts with Bottle and Bokeh</title>
 </head>
 <body>
  <h1>Bugs found over the past {{ bars_count }} days</h1>
 </body>
</html>
"""


@route('/<num_bars:int>/')
def chart(num_bars):
    """Returns a simple template stating the number of bars that should
    be generated when the rest of the function is complete.
    """
    if num_bars <= 0:
        num_bars = 1
    return template(TEMPLATE_STRING, bars_count=num_bars)


if __name__ == '__main__':
    run(host='127.0.0.1', port=8000, debug=False, reloader=True)
