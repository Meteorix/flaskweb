Example Flaskweb
================
```
$ pip install -U flaskweb

# migrate db after changing db.models
$ cd example
$ flask db init
$ flask db migrate
$ flask db upgrade

# run server
$ python wsgi.py
```
*   http://127.0.0.1:5000/  # for app index page
*   http://127.0.0.1:5000/main  # for dev index page
*   http://127.0.0.1:5000/admin  # for db admin page
*   http://127.0.0.1:5000/apidocs  # for swagger ui

# Deployment
```shell
gunicorn -c gunicorn_config.py wsgi:app
```

# Distribution

Distribute example project using [setup.py](./setup.py)

```bash
cd example
python setup.py build
python setup.py sdist --formats=zip
```

Or cythonize and dist as wheel for better encryption

```bash
python setup.py bdist_wheel
```
