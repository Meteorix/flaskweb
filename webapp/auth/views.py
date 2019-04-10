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

    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).one()
        login_user(user)

        return redirect(request.args.get("next") or url_for("main.index"))

    return render_template("login.html", form=form)


@bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))
