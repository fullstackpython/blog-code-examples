from flask import send_from_directory, render_template
from flask import redirect, g
from app import app, oidc, okta_client


@app.before_request
def before_request():
    if oidc.user_loggedin:
        g.user = okta_client.get_user(oidc.user_getfield("sub"))
    else:
        g.user = None


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
@oidc.require_login
def repositories():
    return render_template('repositories.html')


@app.route("/login")
@oidc.require_login
def login():
    return redirect(url_for(".repositories"))


@app.route("/logout")
def logout():
    oidc.logout()
    return redirect(url_for(".landing_page"))
