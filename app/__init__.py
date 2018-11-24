from flask import Flask

IssueTracker = Flask(__name__)

from app import index
from app import forgotpwd
from app import newuser
from app import issuesmain
from app import signOut
