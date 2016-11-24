import webapp2
from src.user_account.index import Index
from src.user_account.login import Login
from src.user_account.signup import Signup
from src.user_account.logout import Logout
from src.core.blog import Blog
from src.core.new_post import NewPost
from src.core.post_page import PostPage
from src.core.my_post import MyPost
from src.core.comment import Comment

app = webapp2.WSGIApplication(
    [('/', Index),
     ('/login', Login),
     ('/signup', Signup),
     ('/logout', Logout),
     ('/blog', Blog),
     ('/blog/my', MyPost),
     ('/blog/post', NewPost),
     ('/blog/post/([0-9]+)', PostPage),
     ('/blog/comment', Comment)],
    debug=True)
