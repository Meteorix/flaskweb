# coding=utf-8
# Created by Meteorix at 2019/4/10

from flaskweb.app import create_app, db, admin, ModelView

import todoapp.models as todo_models
import todoapp.views as todo_views


app = create_app("debug")
app.register_blueprint(todo_views.bp)
# admin
admin.add_view(ModelView(todo_models.Todo, db.session))
admin.add_view(ModelView(todo_models.TodoItem, db.session))


if __name__ == "__main__":
    # for debug only
    from gevent.pywsgi import WSGIServer
    ip, port = "0.0.0.0", 5000
    print("gevent server staring on http://%s:%s" % (ip, port))
    WSGIServer((ip, int(port)), app).serve_forever()
