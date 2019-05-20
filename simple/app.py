from flaskweb.app import create_app, gevent_run
from flask_login import current_user
from flask import render_template, jsonify

app = create_app("debug")


@app.route("/")
def index():
    return render_template("main.html")


@app.route("/whoami")
def whoami():
    """Example endpoint returning current user
    Api for current user info
    ---
    responses:
      200:
        description: current user info
        examples:
            json: { "name": "meteorix" }
    """
    if current_user.is_authenticated:
        name = current_user.username
    else:
        name = "anonymous"
    return jsonify({"name": name})



if __name__ == "__main__":
    gevent_run(app)
