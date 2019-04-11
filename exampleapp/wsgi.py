# coding=utf-8
# Created by Meteorix at 2019/4/10

from flaskweb.app import create_app, db, admin, ModelView

import models
import views


app = create_app("debug")
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
