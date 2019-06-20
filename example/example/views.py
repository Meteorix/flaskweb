# encoding=utf-8
from flask import request, Blueprint, render_template, redirect, url_for, jsonify, current_app as app
from flask_login import login_required, current_user
from flaskweb.app import db
from flaskweb.auth.views import check_user_login
from flasgger import swag_from
from .models import Todo, TodoItem
import os


basedir = os.path.dirname(__file__)
modname = "example"
bp = Blueprint(modname, modname, static_url_path="",
               static_folder=os.path.join(basedir, "static"),
               template_folder=os.path.join(basedir, "templates"))


@bp.route("/")
def index():
    # create static/index.html, or default to debug index page
    app.logger.info("got you at index")
    app.logger.error("got a fake error")
    return render_template(["index.html", "debug.html"])


@bp.route("/api/login", methods=["POST"])
def login():
    # rewrite login api
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")
    if check_user_login(username, password):
        return redirect(url_for(modname + ".index"))
    else:
        return "login error", 400


@login_required
@bp.route("/todo", methods=["GET", "POST"])
@swag_from("specs/todo_get.yml", methods=["GET"])
@swag_from("specs/todo_post.yml", methods=["POST"])
def todo():
    if request.method == "GET":
        todos = Todo.query.all()
        todos = [i.to_dict() for i in todos]
        return jsonify(todos)
    else:
        todo = Todo.create(request.form['name'], current_user, request.form['tag'])
        db.session.add(todo)
        db.session.commit()
        return jsonify(todo.to_dict())


@login_required
@bp.route("/todo/<int:tid>", methods=["GET", "POST"])
@swag_from("specs/todoitem_get.yml", methods=["GET"])
@swag_from("specs/todoitem_post.yml", methods=["POST"])
def todo_item(tid):
    if request.method == "GET":
        todo = TodoItem.query.filter_by(tid=tid).all()
        res = [t.to_dict() for t in todo]
        return jsonify(res)
    else:
        task = request.form['task'].strip()
        todo = TodoItem.create(tid, task, current_user)
        db.session.add(todo)
        db.session.commit()
        return jsonify(todo.to_dict())


@login_required
@bp.route('/upload', methods=["POST"])
@swag_from("specs/upload_post.yml", methods=["POST"])
def upload():
    fs = request.files['file']
    upload_dir = app.config["UPLOAD_DIR"]
    if not os.path.exists(upload_dir):
        os.makedirs(upload_dir)
    filepath = os.path.join(upload_dir, fs.filename)
    app.logger.info("saving %s to %s" % (fs, filepath))
    fs.save(filepath)
    return jsonify({"result": "ok"})
