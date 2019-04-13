from flaskweb.app import create_app, gevent_run
from flask import render_template

app = create_app("debug")


@app.route("/")
def index():
    return render_template("main.html")


if __name__ == "__main__":
    gevent_run(app)
