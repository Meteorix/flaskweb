Example Flask Web
=================
```
$ pip install -U flaskweb

# migrate db after changing db.models
$ cd example
$ flask db init
$ flask db upgrade
$ flask db migrate

# run server
$ python wsgi.py
```
*   http://127.0.0.1:5000/  # for app index page
*   http://127.0.0.1:5000/main  # for dev index page
*   http://127.0.0.1:5000/admin  # for db admin page
*   http://127.0.0.1:5000/swagger  # for swagger ui
