from flaskweb.app import create_app, gevent_run
from flask_login import current_user
from flasgger import swag_from
from flask import render_template, jsonify, request, send_file
import subprocess as sb
import os


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


@app.route('/upload', methods=["POST"])
def upload():
    """
    Api for upload and download file
    ---
    parameters:
    - name: file
      required: false
      in: formData
      type: file
    responses:
      200:
        description: download file or error info
        examples:
            json: { "error": "...", "success": false}
    """
    fs = request.files['file']
    upload_dir = "uploads"
    if not os.path.exists(upload_dir):
        os.makedirs(upload_dir)
    filepath = os.path.join(upload_dir, fs.filename)
    fs.save(filepath)
    # example: call external programs
    out_path = filepath + ".copy"
    print(filepath, out_path)
    proc = sb.Popen(["cp", filepath, out_path], stdout=sb.PIPE, stderr=sb.STDOUT)
    out, err = proc.communicate()
    app.logger.info(out.decode("gbk"))

    if proc.returncode == 0:
        return send_file(os.path.abspath(out_path), as_attachment=True)
    else:
        return jsonify({"error": out, "success": False})


if __name__ == "__main__":
    gevent_run(app, port=5002)
