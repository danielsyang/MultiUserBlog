from src.handler import Handler


class Index(Handler):
    def get(self):
        self.render('index.html')
