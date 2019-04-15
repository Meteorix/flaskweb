from flask import redirect, request, url_for, render_template, Blueprint
from flask_login import LoginManager, login_user, logout_user, login_required
from .models import User
from .forms import LoginForm

bp = Blueprint("auth", "auth")

login_manager = LoginManager()
login_manager.login_view = "auth.login"


@login_manager.user_loader
def load_user(uid):
    return User.query.get(uid)


@bp.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    nexturl = request.args.get("next", "")

    if form.validate_on_submit():
        if check_user_login(form.username.data, form.password.data):
            return redirect(nexturl or url_for("main.index"))

    return render_template("login.html", form=form, nexturl=nexturl)


def check_user_login(username, password):
    user = User.query.filter_by(username=username).one()
    if user.check_password(password):
        login_user(user)
        return True
    return False


@bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))
