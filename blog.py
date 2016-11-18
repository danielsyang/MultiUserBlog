import webapp2
from src.login import Login
from src.signup import Signup


app = webapp2.WSGIApplication(
    [('/', Login),
    ('/signup', Signup)],
    debug=True)
