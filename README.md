flask-webapp
========
boilerplate flask webapp for AI webservice

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
*   rest
*   swagger
*   gunicorn

## todo
*   jwt
*   nginx.conf for deployment
*   config
*   logger

development
========
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


deployment
========
```
./run_server.sh
```

todo: nginx

thanks
======
*   https://github.com/miguelgrinberg/flasky
*   https://github.com/JackStouffer/Flask-Foundation
