# imports for both Flask and Okta connection
from os import environ
from flask import Flask, Response, redirect, g, url_for
from flask_oidc import OpenIDConnect
from okta import UsersClient


app = Flask(__name__)
# secret credentials for Okta connection
app.config["OIDC_CLIENT_SECRETS"] = "openidconnect_secrets.json"
app.config["OIDC_COOKIE_SECURE"] = False
app.config["OIDC_CALLBACK_ROUTE"] = "/oidc/callback"
app.config["OIDC_SCOPES"] = ["openid", "email", "profile"]
app.config["SECRET_KEY"] = environ.get("SECRET_KEY")
app.config["OIDC_ID_TOKEN_COOKIE_NAME"] = "oidc_token"
# instantiate OpenID client to handle user session
oidc = OpenIDConnect(app)
# Okta client will determine if a user has an appropriate account
okta_client = UsersClient(environ.get("OKTA_ORG_URL"),
                          environ.get("OKTA_AUTH_TOKEN"))


@app.before_request
def before_request():
    if oidc.user_loggedin:
        g.user = okta_client.get_user(oidc.user_getfield("sub"))
    else:
        g.user = None


@app.route("/lair")
@oidc.require_login
def lair():
    thundercats_lair = '<html><head><title>Thundercats, hoooo!</title></head><body><h1>Thundercats now hidden lair.</h1><iframe src="https://giphy.com/embed/ahXtBEbHiraxO" width="480" height="273" frameBorder="0" class="giphy-embed" allowFullScreen></iframe><p><a href="https://giphy.com/gifs/retro-cartoons-thundercats-ahXtBEbHiraxO">via GIPHY</a></p></body></html>'
    return Response(thundercats_lair)


@app.route("/")
def landing_page():
    return Response("Thundercats, Thundercats, hoooooooooooo!")


@app.route("/login")
@oidc.require_login
def login():
    """Force user to login and then redirect them to the lair.
    """
    return redirect(url_for(".lair"))


@app.route("/logout")
def logout():
    oidc.logout()
    return redirect(url_for(".landing_page"))
