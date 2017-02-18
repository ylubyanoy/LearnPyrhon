from datetime import datetime
from flask_login import UserMixin, AnonymousUserMixin
from markdown import markdown
import bleach
from . import db, login_manager


@login_manager.user_loader
def load_user(user_id):
    return Usersdb.query.get(int(user_id))


class Usersdb(UserMixin, db.Model):
    __tablename__ = 'users'

    user_id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(200), unique=True, index=True)
    user_pass = db.Column(db.String(50))
    email = db.Column(db.String(65), unique=True, index=True)
    company_name = db.Column(db.String(65))
    articles = db.relationship('Articles', backref='username', lazy='dynamic')

    @property
    def is_authenticated(self):
        return True

    @property
    def is_active(self):
        return True

    @property
    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self.user_id)

    def __repr__(self):
        return '<Пользователь - {}>'.format(self.user_name)


class Articles(UserMixin, db.Model):
    __tablename__ = 'articles'

    article_id = db.Column(db.Integer, primary_key=True)
    a_title = db.Column(db.String(200))
    a_body = db.Column(db.Text)
    a_body_html = db.Column(db.Text)
    a_timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    userid = db.Column(db.Integer, db.ForeignKey('users.user_id'))

    @staticmethod
    def on_changed_body(target, value, oldvalue, initiator):
        allowed_tags = ['a', 'abbr', 'acronym', 'b', 'blockquote', 'code',
                        'em', 'i', 'li', 'ol', 'pre', 'strong', 'ul',
                        'h1', 'h2', 'h3', 'p']
        target.a_body_html = bleach.linkify(bleach.clean(
            markdown(value, output_format='html'),
            tags=allowed_tags, strip=True))

    def __repr__(self):
        return '<Статья - {}>'.format(self.a_title)

db.event.listen(Articles.a_body, 'set', Articles.on_changed_body)
