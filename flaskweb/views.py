from flask import Blueprint, render_template, redirect
from flask_login import login_required, current_user
import os


basedir = os.path.dirname(os.path.abspath(__file__))
bp = Blueprint("main", "main", url_prefix="/main",
               static_url_path="/static",
               static_folder=os.path.join(basedir, "static"),
               template_folder=os.path.join(basedir, "templates"))


@bp.route('/')
def index():
    return render_template('main.html')


@bp.route('/user')
@login_required
def user():
    return 'hello world %s' % current_user.username
