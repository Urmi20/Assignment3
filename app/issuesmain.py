from flask import render_template, redirect, url_for, session
from app import IssueTracker
from app.tools.dbTools import DataBaseManager

@IssueTracker.route('/main_issue_list')
def render_main_issue_list():
    if 'authorized' in session and session['authorized'] is True:
        issues = DataBaseManager.get_issues()

        return render_template("mainissuelist.html")

    return redirect(url_for("index"))