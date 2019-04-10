from flask import render_template, Blueprint
from flask_login import login_required, current_user


bp = Blueprint("main", "main")


@bp.route('/')
def index():
    return render_template('index.html')


@bp.route('/user')
@login_required
def user():
    return 'hello world %s' % current_user.username
