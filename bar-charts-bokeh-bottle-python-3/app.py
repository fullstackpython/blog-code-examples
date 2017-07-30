import os
import bottle
import random
from bokeh.models import (HoverTool, FactorRange, Plot, LinearAxis, Grid,
                          Range1d)
from bokeh.models.glyphs import VBar
from bokeh.plotting import figure
from bokeh.charts import Bar
from bokeh.embed import components
from bokeh.models.sources import ColumnDataSource
from bottle import route, run, template


app = bottle.default_app()

TEMPLATE_STRING = """
<html>
 <head>
  <title>Bar charts with Bottle and Bokeh</title>
  <link href="http://cdn.pydata.org/bokeh/release/bokeh-0.12.6.min.css" rel="stylesheet">
  <link href="http://cdn.pydata.org/bokeh/release/bokeh-widgets-0.12.6.min.css" rel="stylesheet">
 </head>
 <body>
  <h1>Bugs found over the past {{ bars_count }} days</h1>
  {{ !the_div }}
  <script src="http://cdn.pydata.org/bokeh/release/bokeh-0.12.6.min.js"></script>
  <script src="http://cdn.pydata.org/bokeh/release/bokeh-widgets-0.12.6.min.js"></script>
  {{ !the_script }}
 </body>
</html>
"""


@route('/<num_bars:int>/')
def chart(num_bars):
    """Creates a bar chart with the desired number of bars in a chart."""
    if num_bars <= 0:
        num_bars = 1
    data = {"days": [], "bugs": [], "costs": []}
    for i in range(1, num_bars + 1):
        data['days'].append(i)
        data['bugs'].append(random.randint(1,100))
        data['costs'].append(random.uniform(1.00, 1000.00))

    hover = create_hover_tool()
    plot = create_bar_chart(data, "Bugs found per day", "days",
                            "bugs", hover)
    script, div = components(plot)
    return template(TEMPLATE_STRING, bars_count=num_bars,
                      the_div=div, the_script=script)


def create_hover_tool():
    # we'll code this function in a moment
    return None


def create_bar_chart(data, title, x_name, y_name, hover_tool=None,
                     width=1200, height=300):
    """Creates a bar chart plot with the exact styling for the centcom
       dashboard. Pass in data as a dictionary, desired plot title,
       name of x axis, y axis and the hover tool HTML.
    """
    source = ColumnDataSource(data)
    xdr = FactorRange(factors=data[x_name])
    ydr = Range1d(start=0,end=max(data[y_name])*1.5)

    tools = []
    if hover_tool:
        tools = [hover_tool,]

    plot = figure(title=title, x_range=xdr, y_range=ydr, plot_width=width,
                  plot_height=height, h_symmetry=False, v_symmetry=False,
                  min_border=10, toolbar_location="above", tools=tools,
                  responsive=True, outline_line_color="#666666")

    glyph = VBar(x=x_name, top=y_name, bottom=0, width=.8,
                 fill_color="#6599ed")
    plot.add_glyph(source, glyph)

    xaxis = LinearAxis()
    yaxis = LinearAxis()

    plot.add_layout(Grid(dimension=0, ticker=xaxis.ticker))
    plot.add_layout(Grid(dimension=1, ticker=yaxis.ticker))
    plot.toolbar.logo = None
    plot.min_border_top = 0
    plot.xgrid.grid_line_color = None
    plot.ygrid.grid_line_color = "#999999"
    plot.yaxis.axis_label = "Bugs found"
    plot.ygrid.grid_line_alpha = 0.1
    plot.xaxis.axis_label = "Days after app deployment"
    plot.xaxis.major_label_orientation = 1
    return plot


if __name__ == '__main__':
    run(host='127.0.0.1', port=8000, debug=False, reloader=True)
