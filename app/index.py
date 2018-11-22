from flask import render_template, session, redirect, url_for, request
from app import IssueTracker
from app.tools.hashTools import Hash
from app.tools.dbTools import DataBaseManager

IssueTracker.secret_key = "SecretUserUI##187782####"


@IssueTracker.route("/", methods=['GET'])
def index():
    if 'authorized' in session and session['authorized'] is True:
        return redirect(url_for("render_gallery"))

    return render_template("index.html", type="user")


def create_session_for(username, password):
    pwd_manager = Hash()
    if pwd_manager.check_password(username, password):
        session['user'] = username
        session['authorized'] = True

        dbm = DataBaseManager()
        session['type'] = dbm.get_user_type(username)

        return True
    return False


@IssueTracker.route('/authenticate_user', methods=['POST'])
def authenticate_user():
    username = request.form.get('username')
    password = request.form.get('password')

    if create_session_for(username, password):
        return redirect(url_for('render_gallery'))

    return render_template("index.html", error=True, username=username, type="user")
