from os import environ
from flask import Flask, Response


app = Flask(__name__)
app.config["DEBUG"] = True
# secret credentials for Okta connection
app.config["OIDC_CLIENT_SECRETS"] = "client_secrets.json"
app.config["OIDC_COOKIE_SECURE"] = False
app.config["OIDC_CALLBACK_ROUTE"] = "/oidc/callback"
app.config["OIDC_SCOPES"] = ["openid", "email", "profile"]
app.config["SECRET_KEY"] = environ.get("SECRET_KEY")
app.config["OIDC_ID_TOKEN_COOKIE_NAME"] = "oidc_token"
# instantiate Open ID client to handle user session
oidc = OpenIDConnect(app)
# Okta client will determine if a user has an appropriate account
okta_client = UsersClient(environ.get("OKTA_ORG_URL"),
                          environ.get("OKTA_AUTH_TOKEN"))


@app.route("/lair")
def lair():
    return Response("Thundercats (supposed to be hidden) lair.")


@app.route("/")
def landing_page():
    return Response("Thundercats, Thundercats, hoooooooooooo!")

