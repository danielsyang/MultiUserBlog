from google.appengine.ext import db

from src.user_account.security import is_pass_valid
from src.user_account.security import make_password_hash


class User(db.Model):
    name = db.StringProperty(required=True)
    password_hash = db.StringProperty(required=True)
    email = db.StringProperty()

    @classmethod
    def user_by_id(cls, user_id):
        return User.get_by_id(user_id)

    @classmethod
    def user_by_name(cls, user_name):
        return User.all().filter('name = ', user_name).get()

    @classmethod
    def user_register(cls, name, password, email):
        pass_hash = make_password_hash(name, password)
        return User(name=name, password_hash=pass_hash, email=email)

    @classmethod
    def login(cls, name, password):
        user = cls.user_by_name(name)

        if user and is_pass_valid(name, password, user.password_hash):
            return user
