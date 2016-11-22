import webapp2
from src.user_account.index import Index
from src.user_account.login import Login
from src.user_account.signup import Signup
from src.user_account.logout import Logout
from src.core.blog import Blog
from src.core.post_page import PostPage

app = webapp2.WSGIApplication(
    [('/', Index),
     ('/login', Login),
     ('/signup', Signup),
     ('/blog', Blog),
     ('/logout', Logout),
     ('/blog/post', PostPage)],
    debug=True)
