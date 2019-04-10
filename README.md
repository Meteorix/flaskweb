flask-webapp
========
boilerplate webapp with flask

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

development
========
## frontend

nothing to do

## backend
```
# setup virtualenv 
$ virtualenv env
$ source env/bin/activate
$ source env/Scripts/activate  # on windows
$ pip install -r requirements.txt

# migrate db after changing
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