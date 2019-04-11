from flask_script import Manager
from flask_migrate import MigrateCommand
from wsgi import app, db


manager = Manager(app)
manager.add_command('db', MigrateCommand)


@manager.command
def gvserver(ip="0.0.0.0", port=5000):
    from gevent.pywsgi import WSGIServer
    print("gevent server staring on %s %s" % (ip, port))
    WSGIServer((ip, int(port)), app).serve_forever()


@manager.shell
def make_shell_context():
    import webapp
    return dict(app=app, db=db, flask_react_app=webapp)


if __name__ == "__main__":
    manager.run()
