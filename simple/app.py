from flaskweb.app import create_app, gevent_run
from flask_login import current_user
from flasgger import swag_from
from flask import render_template, jsonify, request

app = create_app("debug")


@app.route("/")
def index():
    return render_template("debug.html")


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


@app.route("/post_or_get_example", methods=["GET", "POST"])
@swag_from("simple_get.yml", methods=["GET"])
@swag_from("simple_post.yml", methods=["POST"])
def post_or_get_example():
    if request.method == "GET":
        get_input = request.args["get_input"]
        get_output = "output of " + get_input
        return jsonify({"get_output": get_output})
    else:
        post_input = request.form["post_input"]
        post_output = "output of " + post_input
        return jsonify({"post_output": post_output})


if __name__ == "__main__":
    gevent_run(app)
