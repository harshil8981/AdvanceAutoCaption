from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Mrkiller Developer"


if __name__ == "__main__":
    app.run()