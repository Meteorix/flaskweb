from flask import Blueprint, render_template, current_app as app
from flask_login import login_required, current_user


bp = Blueprint("main", "main")


@bp.route('/')
def index():
    app.logger.info("got you")
    return render_template('index.html')


@bp.route('/user')
@login_required
def user():
    app.logger.error("got a fake error")
    return 'hello world %s' % current_user.username
