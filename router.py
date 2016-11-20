import webapp2
from src.login import Login
from src.signup import Signup
from src.blog import Blog

app = webapp2.WSGIApplication(
    [('/', Login),
     ('/signup', Signup),
     ('/blog',Blog)],
    debug=True)
