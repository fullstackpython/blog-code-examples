from flask import send_from_directory, render_template
from app import app


@app.route('/js/<path:path>')
def send_js(path):
    return send_from_directory('js', path)


@app.route('/css/<path:path>')
def send_css(path):
    return send_from_directory('css', path)


@app.route("/")
def dashboard():
    return render_template('dashboard.html')


@app.route("/repositories")
def repositories():
    return render_template('repositories.html')
