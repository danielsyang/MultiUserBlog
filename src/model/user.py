from google.appengine.ext import db
from security import make_password_hash
from security import is_pass_valid


class User(db.Model):
    name = db.StringProperty(required=True)
    password_hash = db.StringProperty(required=True)
    email = db.StringProperty()

    @classmethod
    def user_by_id(cls, user_id):
        return cls.get_by_id(user_id)

    @classmethod
    def user_by_name(cls, user_name):
        return cls.all().filter('name=', user_name).get()

    @classmethod
    def user_register(cls, name, password, email):
        pass_hash = make_password_hash(name, password)
        return cls(name=name, password_hash=pass_hash, email=email)


    @classmethod
    def login(cls, name, password):
        user = cls.user_by_name(name)

        if user and is_pass_valid(name, password, user.password_hash):
            return user

