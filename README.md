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
$ source venv/Scripts/activate  # git-bash on windows
$ pip install -e .

# migrate db after changing db.models
$ cd example
$ flask db init
$ flask db upgrade
$ flask db migrate
$ flask db --help

# run server
$ python wsgi.py
```
*   http://127.0.0.1:5000/  # for app index page
*   http://127.0.0.1:5000/main  # for dev index page
*   http://127.0.0.1:5000/admin  # for db admin page
*   http://127.0.0.1:5000/swagger  # for swagger ui


# deployment
```
$ python wsgi.py
```

todo: gunicorn / nginx / docker

# thanks
*   https://github.com/miguelgrinberg/flasky
*   https://github.com/JackStouffer/Flask-Foundation
