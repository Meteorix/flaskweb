from webapp.app import db
from datetime import datetime
import json


class Todo(db.Model):

    __tablename__ = 'todo'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    tag = db.Column(db.String(80))
    pub_date = db.Column(db.DateTime)
    uid = db.Column(db.Integer, db.ForeignKey('user.id'))
    items = db.relationship('TodoItem', backref='todo', lazy='dynamic')

    @classmethod
    def create(cls, name, user, tag="", pub_date=None):
        self = cls()
        self.name = name
        self.tag = tag
        if pub_date is None:
            pub_date = datetime.utcnow()
        self.pub_date = pub_date
        self.uid = user.id
        return self

    def __repr__(self):
        return '<Todo %r>' % self.name

    def to_dict(self):
        d = {}
        for column in self.__table__.columns:
            value = getattr(self, column.name)
            d[column.name] = str(value)
        return d

    def to_json(self):
        return json.dumps(self.to_dict())


class TodoItem(db.Model):

    __tablename__ = 'todo_item'

    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String(80))
    pub_date = db.Column(db.DateTime)
    uid = db.Column(db.Integer, db.ForeignKey('user.id'))
    tid = db.Column(db.Integer, db.ForeignKey('todo.id'))

    @classmethod
    def create(cls, tid, task, user, pub_date=None):
        self = cls()
        self.tid = tid
        self.task = task
        if pub_date is None:
            pub_date = datetime.utcnow()
        self.pub_date = pub_date
        self.uid = user.id
        return self

    def __repr__(self):
        return '<TodoItem %r>' % self.task

    def to_dict(self):
        d = {}
        for column in self.__table__.columns:
            d[column.name] = str(getattr(self, column.name))
        return d

    def to_json(self):
        return json.dumps(self.to_dict())
