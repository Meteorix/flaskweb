flask-webapp
============
boilerplate flask webapp for AI webservice or any web project

# features
## frontend

*   bootstrap
*   jquery
*   flask-admin
*   flask-swagger

## backend
*   flask
*   sqlalchemy
*   login
*   admin
*   restplus
*   swagger
*   gunicorn
*   config
*   logger

## todo
*   use as a 3rd library
*   nginx.conf for deployment
*   jwt
*   setup.py
*   cythonize
*   pyinstaller
*   dockerfile

# development
## frontend

nothing to do

## backend
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
$ python -u debug_server.py

# more scripts
$ python manage.py runserver
$ python manage.py shell
$ python manage.py gvserver

```
*   http://127.0.0.1:5000/  # for index page
*   http://127.0.0.1:5000/admin  # for db admin
*   http://127.0.0.1:5000/swagger  # for swagger api


# deployment
```
./run_server.sh
```

todo: nginx / docker

# thanks
*   https://github.com/miguelgrinberg/flasky
*   https://github.com/JackStouffer/Flask-Foundation
