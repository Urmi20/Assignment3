from flask import render_template, redirect, url_for, session, request
from app import IssueTracker
from app.tools.dbTools import DataBaseManager
from app.tools.pdfTools import PdfGenerator
from app.tools.pagination import Pagination


@IssueTracker.route('/main_issue_list')
def render_main_issue_list():
    if 'authorized' in session and session['authorized'] is True:
        status_input = request.form.get('status')
        project_input = request.form.get('project')
        discipline_input = request.form.get('discipline')
        sentiment_input = request.form.get('sentiment')
        # document_input = request.form.get('document')

        issues, last_evaluated_key = Pagination.page_data(None, project_input, None, discipline_input, sentiment_input, status_input)
        projects = DataBaseManager.get_projects()
        disciplines = DataBaseManager.get_disciplines()
        lists=['open','closed']

        return render_template("issue.html", issues=issues, projects=projects, disciplines=disciplines,lists=lists)

    return redirect(url_for("index"))


@IssueTracker.route('/export_to_pdf', methods=['POST'])
def export_to_pdf():
    if 'authorized' in session and session['authorized'] is True:
        issues = DataBaseManager.get_issues()
        pdf = PdfGenerator.format_pdf(issues)

        return PdfGenerator.create_pdf_file(pdf)
    return redirect(url_for("index"))
