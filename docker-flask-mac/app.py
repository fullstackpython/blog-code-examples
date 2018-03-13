from flask import Flask, Response


app = Flask(__name__)


@app.route("/")
def hello(request):
    return Response("Hello from a Flask app within your Docker container!")


if __name__ == "__main__":
    app.run("0.0.0.0", port=80, debug=True)
