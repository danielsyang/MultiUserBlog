from handler import Handler


class Login(Handler):
    def get(self):
        self.render("login.html", text_value="")

    def post(self):
        print "WHAT THE FUCK"
