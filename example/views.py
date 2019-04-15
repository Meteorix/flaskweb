# encoding=utf-8
from flask import request, Blueprint, render_template, redirect, current_app as app
from flask_restplus import Namespace, Resource, reqparse, fields
from werkzeug.datastructures import FileStorage
from flask_login import login_required, current_user
from flaskweb.app import db
from models import Todo, TodoItem
import os


basedir = os.path.dirname(__file__)
print(__name__)
bp = Blueprint("example", "example", static_url_path="",
               static_folder=os.path.join(basedir, "dist"),
               template_folder=os.path.join(basedir, "dist"))
api = Namespace("example")


@bp.route("/")
def index():
    # create dist/index.html, or default to demo index page
    app.logger.info("got you at index")
    app.logger.error("got a fake error")
    return render_template(["index.html", "main.html"])


@bp.route("/api/login", methods=["POST"])
def login():
    return redirect("/login")


@api.route('/todo')
class Todos(Resource):

    post_parser = api.model('todo post', {
        'name': fields.String(desciption='task todo'),
        'tag': fields.String(),
    })

    @login_required
    def get(self):
        todos = Todo.query.all()
        todos = [i.to_dict() for i in todos]
        return todos

    @login_required
    @api.expect(post_parser)
    def post(self):
        data = request.json
        todo = Todo.create(data['name'], current_user, data['tag'])
        db.session.add(todo)
        db.session.commit()
        return todo.to_dict()


@api.route('/todo/<int:tid>')
class TodoItems(Resource):

    post_parser = reqparse.RequestParser()
    post_parser.add_argument('task', type=str, location='form')

    @login_required
    def get(self, tid):
        todo = TodoItem.query.filter_by(tid=tid).all()
        return [t.to_dict() for t in todo]

    @login_required
    @api.expect(post_parser)
    def post(self, tid):
        task = request.form['task'].strip()
        todo = TodoItem.create(tid, task, current_user)
        db.session.add(todo)
        db.session.commit()
        return todo.to_dict()


@api.route('/upload')
class Upload(Resource):
    upload_parser = api.parser()
    upload_parser.add_argument('file', location='files', type=FileStorage, required=True)

    @login_required
    @api.expect(upload_parser)
    def post(self):
        fs = request.files['file']
        upload_dir = app.config["UPLOAD_DIR"]
        if not os.path.exists(upload_dir):
            os.makedirs(upload_dir)
        filepath = os.path.join(upload_dir, fs.filename)
        app.logger.info("saving %s to %s" % (fs, filepath))
        fs.save(filepath)
        return {"result": "ok"}
