import re
from handler import Handler
from model.security import make_secure_value
from model.security import check_secure_value
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
    pass


class Signup(Handler):
    def set_cookie(self, name, val):
        cookie_value = make_secure_value(val)
        self.response.headers.add_header(
            'Set-Cookie',
            '%s|%s; Path=/' % (name, cookie_value))

    def read_cookie(self, name):
        cookie_val = self.request.cookies.get(name)

        if cookie_val:
            if check_secure_value(cookie_val):
                return True

        return False

    def get(self):
        self.render('signup.html', text_value='')

    def post(self):
        self.username = self.request.get('userLogin')
        self.password = self.request.get('userPass')
        self.email = self.request.get('userEmail')

        user = User.user_by_name()
        print "WHAT THE FUCK"
