from flask import redirect, request, url_for, flash, render_template, Blueprint, current_app
from flask_login import LoginManager, login_user, logout_user, login_required
from werkzeug.security import generate_password_hash
from .models import db, User
from .forms import LoginForm, RegistrationForm

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
            return redirect(nexturl or current_app.config.get("LOGIN_REDIRECT_URL") or url_for("main.index"))

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


@bp.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        pswd = generate_password_hash(form.password.data)
        # todo: auto activate users in debug mode
        active = True if current_app.debug else False
        user = User(email=form.email.data,
                    username=form.username.data,
                    password=pswd,
                    active=active)
        db.session.add(user)
        db.session.commit()
        # todo: email verification process
        flash('Please ask website admin to activate your account')
        return redirect(url_for('auth.login'))
    return render_template('register.html', form=form)
