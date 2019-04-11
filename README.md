flask-webapp
============
The complete web framework from dev to production

# installation
```bash
# git clone and install; git pull for later updates
git clone ssh://git@gitlab.shannonai.com:2222/liuxin/flask-webapp.git
pip install -e flask-webapp

# or use one cmd
pip install -U git+ssh://git@gitlab.shannonai.com:2222/liuxin/flask-webapp.git
```

# features
*   flask
*   sqlalchemy
*   config
*   logger
*   user login
*   db admin
*   restful api with swagger ui
*   gunicorn/gevent deployment
*   use as a 3rd library
*   frontend with bootstrap/jquery

## todo
*   nginx.conf for deployment
*   jwt
*   setup.py
*   cythonize
*   pyinstaller
*   dockerfile

# development
```
# setup virtualenv 
$ virtualenv venv
$ source venv/bin/activate
$ source venv/Scripts/activate  # on windows
$ pip install -r requirements.txt

# migrate db after changing db.models
$ python manage.py db init
$ python manage.py db migrate
$ python manage.py db upgrade
$ python manage.py db --help

# run server
$ PYTHONPATH=. python -u exampleapp/wsgi.py

# more scripts
$ python manage.py runserver
$ python manage.py shell
$ python manage.py gvserver

```
*   http://127.0.0.1:5000/  # for app index page
*   http://127.0.0.1:5000/main  # for dev index page
*   http://127.0.0.1:5000/admin  # for db admin page
*   http://127.0.0.1:5000/swagger  # for swagger ui


# deployment
```
$ PYTHONPATH=. python -u exampleapp/wsgi.py
```

todo: nginx / docker

# thanks
*   https://github.com/miguelgrinberg/flasky
*   https://github.com/JackStouffer/Flask-Foundation
