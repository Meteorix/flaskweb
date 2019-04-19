"""db models."""
from flaskweb.app import db
from werkzeug.security import check_password_hash


class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(40))
    password = db.Column(db.String(120))
    email = db.Column(db.String(40))
    authenticated = db.Column(db.Boolean, default=False)
    active = db.Column(db.Boolean, default=False)
    is_admin = db.Column(db.Boolean, default=False)

    def check_password(self, value):
        return check_password_hash(self.password, value)

    def is_active(self):
        """True, as all users are active."""
        return self.active

    def get_id(self):
        """Return the id to satisfy Flask-Login's requirements."""
        return self.id

    def is_authenticated(self):
        """Return True if the user is authenticated."""
        return self.authenticated

    def is_anonymous(self):
        """False, as anonymous users aren't supported."""
        return False

    def __repr__(self):
        return '<user %r>' % self.username
