from flask import render_template, redirect, url_for, session, request
from app import IssueTracker
from app.tools.dbTools import DataBaseManager
from app.tools.pdfTools import PdfGenerator
from app.tools.pagination import Pagination


@IssueTracker.route('/main_issue_list', methods=['POST', 'GET'])
def render_main_issue_list():
    if 'authorized' in session and session['authorized'] is True:
        documents = list()
        status_input = parse_string(request.form.get('status'))
        project_input = parse_string(request.form.get('project'))
        discipline_input = parse_string(request.form.get('discipline'))
        sentiment_input = parse_string(request.form.get('sentiment'))
        document_input = parse_string(request.form.get('document'))
        last_key = parse_string(request.form.get('db_key'))
        first_page = parse_string(request.form.get('first_page'))
        filter = parse_string(request.form.get('filter'))

        if (not filter and not first_page) or filter:
            first_page = 'first_page'

        if project_input:
            documents = DataBaseManager.get_documents_for(project_input)

        if last_key:
            last_key_dict = eval(last_key)
        else:
            last_key_dict = None

        issues, last_key = Pagination.page_data(last_key_dict, project_input, document_input, discipline_input,
                                                          sentiment_input, status_input)
        projects = DataBaseManager.get_projects()
        disciplines = DataBaseManager.get_disciplines()
        lists = ['Open', 'Closed']

        return render_template("issue.html", issues=issues, projects=projects, documents=documents,
                               disciplines=disciplines, lists=lists, selected_status=status_input,
                               selected_project=project_input, selected_document=document_input,
                               selected_discipline=discipline_input, selected_sentiment=sentiment_input,
                               last_key=last_key, first_page=first_page)

    return redirect(url_for("index"))


@IssueTracker.route('/export_to_pdf', methods=['POST'])
def export_to_pdf():
    if 'authorized' in session and session['authorized'] is True:
        status = parse_string(request.form.get('status'))
        project = parse_string(request.form.get('project'))
        discipline = parse_string(request.form.get('discipline'))
        sentiment = parse_string(request.form.get('sentiment'))
        document = parse_string(request.form.get('document'))

        issues = Pagination.get_all_filtered_issues(project, document, discipline, sentiment, status)
        pdf = PdfGenerator.format_pdf(issues)

        return PdfGenerator.create_pdf_file(pdf)
    return redirect(url_for("index"))


@IssueTracker.route('/change_issue_status', methods=['POST'])
def change_issue_status():
    if 'authorized' in session and session['authorized'] is True:
        id = request.form.get('uid')
        status = request.form.get('status_row')
        DataBaseManager.update_issue_status(id, status)

    return ('', 204)


def parse_string(text):
    if text == "All" or text == "None":
        return None

    return text
