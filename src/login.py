from handler import Handler
from model.user import User


class Login(Handler):
    def get(self):
        self.render("login.html")

    def post(self):
        username = self.request.get('userLogin')
        password = self.request.get('userPass')

        us = User.login(username, password)

        if us:
            self.login(us)
            self.redirect('/blog')
        else:
            print "WHAT THE FUCK"
