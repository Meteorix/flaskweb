# coding=utf-8
# Created by Meteorix at 2019/4/10

import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_restplus import Api


db = SQLAlchemy()


def create_app():
    app = Flask(
        __name__,
        static_url_path='/static',
        static_folder='static',
        template_folder='templates',
    )
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(os.path.dirname(__file__), 'app.db')
    app.config['SECRET_KEY'] = 'some thing secret'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    migrate = Migrate(app, db)

    import webapp.views as main_views
    import webapp.auth.models as auth_models
    import webapp.auth.views as auth_views
    import webapp.todo.models as todo_models
    import webapp.todo.views as todo_views

    auth_views.login_manager.init_app(app)
    app.register_blueprint(main_views.bp)
    app.register_blueprint(auth_views.bp)

    admin = Admin(app)
    admin.add_view(ModelView(auth_models.User, db.session))
    admin.add_view(ModelView(todo_models.Todo, db.session))
    admin.add_view(ModelView(todo_models.TodoItem, db.session))

    api = Api(app, doc="/swagger/")
    api.add_namespace(todo_views.api)

    return app
