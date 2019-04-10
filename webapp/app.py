# coding=utf-8
# Created by Meteorix at 2019/4/10

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_restplus import Api
from flask.logging import default_handler
from logging import Formatter, FileHandler
from webapp.config import configs
import logging


db = SQLAlchemy()


def create_app(config_name):
    app = Flask(
        __name__,
        static_url_path='/static',
        static_folder='static',
        template_folder='templates',
    )
    conf = configs[config_name]
    app.config.from_object(conf)

    # logging
    create_logger(app)

    # db
    db.init_app(app)
    migrate = Migrate(app, db)

    # views
    import webapp.views as main_views
    import webapp.auth.models as auth_models
    import webapp.auth.views as auth_views
    import webapp.todo.models as todo_models
    import webapp.todo.views as todo_views

    auth_views.login_manager.init_app(app)
    app.register_blueprint(main_views.bp)
    app.register_blueprint(auth_views.bp)

    # admin
    admin = Admin(app)
    admin.add_view(ModelView(auth_models.User, db.session))
    admin.add_view(ModelView(todo_models.Todo, db.session))
    admin.add_view(ModelView(todo_models.TodoItem, db.session))

    # swagger
    api = Api(app, doc="/swagger/")
    api.add_namespace(todo_views.api)

    return app


def create_logger(app):
    # log to stderr
    formatter = Formatter('[%(asctime)s] [%(filename)s:%(lineno)d] [%(levelname)s]\t%(message)s')
    default_handler.setFormatter(formatter)

    file_handler = FileHandler(app.config["LOGGING_FILE"])
    file_handler.setFormatter(formatter)
    app.logger.addHandler(file_handler)
    app.logger.setLevel(app.config["LOGGING_LEVEL"])
