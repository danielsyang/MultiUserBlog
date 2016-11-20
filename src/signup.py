import re
from handler import Handler
from model.user import User

USERNAME_REGEX = re.compile(r'^[a-zA-Z0-9_-]{3,20}$')
EMAIL_REGEX = re.compile(r'^[\S]+@[\S]+\.[\S]+$')


def is_username_valid(name):
    if name and USERNAME_REGEX.match(name):
        return True

    return False


def is_email_valid(email):
    if email and EMAIL_REGEX.match(email):
        return True

    return False


def signup_verif(name, password, pass_verif, email):
    result = dict()

    if not is_username_valid(name):
        result['error_username'] = "That is not a valid username."
    elif User.user_by_name(name) is not None:
        result['error_username'] = "Username already exists."

    if not is_email_valid(email):
        result['error_email'] = "That is not a valid email."

    if password != pass_verif:
        result['error_password'] = "Your password didn't match."

    if password == "":
        result['error_password'] = "Your password is invalid."

    return result


class Signup(Handler):
    def get(self):
        self.render('signup.html')

    def post(self):

        email = self.request.get('userEmail')
        password = self.request.get('userPass')
        username = self.request.get('userLogin')
        password_verif = self.request.get('userPassVerif')

        signup = signup_verif(username, password, password_verif, email)

        if signup:
            signup['username'] = username
            signup['email'] = email
            self.render('signup.html', **signup)
        else:
            us = User.user_register(username, password, email)
            us.put()
