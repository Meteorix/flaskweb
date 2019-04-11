# encoding=utf-8
from flask import request, Blueprint
from flask_restplus import Resource, Api, reqparse, fields
from werkzeug.datastructures import FileStorage
from flask_login import login_required, current_user
from webapp.app import db
from todoapp.models import Todo, TodoItem
import os


bp = Blueprint("todoapp", "todoapp")
api = Api(bp, doc="/swagger/", prefix="/api")


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
        filepath = os.path.join("./uploads", fs.filename)
        print("saving %s to %s" % (fs, filepath))
        fs.save(filepath)
        return {"result": "ok"}
