from src.handler import Handler
from src.model.user import User


class Login(Handler):
    def get(self):
        if not self.user:
            self.render("login.html")
        else:
            self.redirect("/blog")

    def post(self):
        username = self.request.get('userLogin')
        password = self.request.get('userPass')

        us = User.login(username, password)

        if us:
            self.login(us)
            self.redirect('/blog')
        else:
            self.render("login.html", text_error="Invalid login!")
