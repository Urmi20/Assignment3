from flask import render_template, session, redirect, url_for, request
from app import IssueTracker
from app.tools.hashTools import Hash
from app.tools.dbTools import DataBaseManager
from app.tools.pagination import Pagination

IssueTracker.secret_key = "SecretUserUI##187782####"


@IssueTracker.route("/", methods=['GET'])
def index():
    if 'authorized' in session and session['authorized'] is True:
        issues, last_evaluated_key = Pagination.scan_page()
        print(issues)
        while last_evaluated_key is not None:
            issues, last_evaluated_key = Pagination.scan_page(last_evaluated_key)
        return redirect(url_for("render_main_issue_list"))

    return render_template("index.html")


def create_session_for(username, password):
    pwd_manager = Hash()
    if pwd_manager.check_password(username, password):
        session['user'] = username
        session['authorized'] = True

        return True
    return False


@IssueTracker.route('/authenticate_user', methods=['POST'])
def authenticate_user():
    username = request.form.get('username')
    password = request.form.get('password')

    if create_session_for(username, password):
        return redirect(url_for('render_main_issue_list'))

    return render_template("index.html", error=True, username=username)
