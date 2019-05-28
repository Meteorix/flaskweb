#coding=utf-8
from example.app import DebugConfig, init_app, gevent_run
import os


basedir = os.path.dirname(os.path.abspath(__file__)) or "."


class MyConfig(DebugConfig):
    # override default Configs
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
    LOGGING_FILE = os.path.join(basedir, "logs", "app.log")
    UPLOAD_DIR = os.path.join(basedir, "uploads")


app = init_app(MyConfig)


if __name__ == "__main__":
    # for debug only
    gevent_run(app, "0.0.0.0", 5000)
