from flask import render_template, redirect, url_for, session
from app import IssueTracker
from app.tools.dbTools import DataBaseManager
from app.tools.pdfTools import PdfGenerator
from app.tools.pagination import Pagination


@IssueTracker.route('/main_issue_list')
def render_main_issue_list():
    if 'authorized' in session and session['authorized'] is True:
        issues, last_evaluated_key = Pagination.scan_page(None, 5, None, None, 'Electrical', None, 'Open')
        projects = DataBaseManager.get_projects()
        disciplines = DataBaseManager.get_disciplines()

        return render_template("issue.html", issues=issues, projects=projects, disciplines=disciplines)
    return redirect(url_for("index"))


@IssueTracker.route('/export_to_pdf', methods=['POST'])
def export_to_pdf():
    if 'authorized' in session and session['authorized'] is True:
        issues = DataBaseManager.get_issues()
        pdf = PdfGenerator.format_pdf(issues)

        return PdfGenerator.create_pdf_file(pdf)
    return redirect(url_for("index"))
