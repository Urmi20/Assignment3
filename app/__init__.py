from flask import Flask

IssueTracker = Flask(__name__)

from app import index
from app import forgotpwd
from app import newuser
# from IssueTracker import gallery
# from IssueTracker import lightbox
# from IssueTracker import signOut
# from IssueTracker import photoupload
# from IssueTracker.tools import dbTools
