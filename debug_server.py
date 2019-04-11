# coding=utf-8
# Created by Meteorix at 2019/4/10

from webapp.app import create_app, db, admin, api, ModelView

import todoapp.models as todo_models
import todoapp.views as todo_views


app = create_app("debug")
# admin
admin.add_view(ModelView(todo_models.Todo, db.session))
admin.add_view(ModelView(todo_models.TodoItem, db.session))
# api
api.add_namespace(todo_views.api)


if __name__ == "__main__":
    app.run()
