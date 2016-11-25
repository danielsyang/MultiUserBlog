from src.handler import Handler


class Index(Handler):
    def get(self):
        if not self.user:
            self.render('index.html')
        else:
            self.redirect("/blog")
