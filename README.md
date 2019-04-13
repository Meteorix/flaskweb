flask-webapp
============
The complete web framework from dev to production

# quickstart
基本语法与flask几乎一样，几行代码即可构建一个web服务器
```python
from flaskweb.app import create_app, gevent_run
from flask import render_template

app = create_app("debug")

@app.route("/")
def index():
    return render_template("main.html")

if __name__ == "__main__":
    gevent_run(app)
```
不一样的地方在于，上面的web服务器自带：
*   用户登录系统
*   orm/migrate
*   db管理页面
*   restapi/swaggerui
*   gevent服务器

try it:
```bash
cd simple
# 初始化数据库，会保存到simple/app.db
flask db init
flask db upgrade
flask db migrate
# 运行gevent服务器
python -u app.py
```
then visit http://127.0.0.1:5000/

A more [sophisticated example](./example)

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
