# coding=utf-8
# Created by Meteorix at 2019/4/10
from flaskweb.app import create_app, db, admin, ModelView
from flaskweb.config import DebugConfig
from example import models
from example import views
import os

basedir = os.path.dirname(__file__)


class MyConfig(DebugConfig):
    # you can write your own
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
    LOGGING_FILE = os.path.join(basedir, "app.log")


app = create_app(MyConfig)
app.register_blueprint(views.bp)
# admin
admin.add_view(ModelView(models.Todo, db.session))
admin.add_view(ModelView(models.TodoItem, db.session))


if __name__ == "__main__":
    # for debug only
    from gevent.pywsgi import WSGIServer
    ip, port = "0.0.0.0", 5000
    print("gevent server staring on http://%s:%s" % (ip, port))
    WSGIServer((ip, int(port)), app).serve_forever()
