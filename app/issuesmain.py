from flask import render_template, request, redirect, url_for, session
from app import IssueTracker


@IssueTracker.route('/main_issue_list')
def render_main_issue_list():
    return render_template("mainissuelist.html")