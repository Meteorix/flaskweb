# coding=utf-8
# Created by Meteorix at 2019/4/10
from flaskweb.app import create_app, gevent_run, db, admin, ModelView
from flaskweb.config import DebugConfig
from . import models
from . import views


def init_app(config=DebugConfig):
    app = create_app(config)
    app.register_blueprint(views.bp)
    # admin
    admin.add_view(ModelView(models.Todo, db.session))
    admin.add_view(ModelView(models.TodoItem, db.session))
    return app
