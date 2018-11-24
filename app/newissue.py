from flask import render_template, session, redirect, url_for, request
from app import IssueTracker
from app.tools.dbTools import DataBaseManager


@IssueTracker.route("/new_issue_landing", methods=['GET', 'POST'])
def new_issue_landing():
    if 'authorized' in session and session['authorized'] is True:
        projects = DataBaseManager.get_projects()
        documents = list()
        disciplines = list()

        selected_project = request.form.get('project')
        selected_document = request.form.get('document')
        selected_discipline = request.form.get('discipline')
        current_issue = request.form.get('issue')
        issues_so_far = request.form.get('issues_so_far')

        if selected_project:
            DataBaseManager.add_project(selected_project)
            documents = DataBaseManager.get_documents_for(selected_project)

        if selected_project and selected_document:
            DataBaseManager.add_document(selected_project, selected_document)
            disciplines = DataBaseManager.get_disciplines()

        if issues_so_far == 'None' or issues_so_far == '[]':
            issues_so_far = ''

        if selected_project and selected_document and selected_discipline and current_issue:
            issues_so_far = issues_so_far + selected_project + " :: " + selected_document + " :: " + selected_discipline + "|" + current_issue + "||"

        return render_template("newissue.html", projects=projects, selected_project=selected_project,
                               documents=documents, selected_document=selected_document, disciplines=disciplines,
                               selected_discipline=selected_discipline, issues_so_far=issues_so_far)

    return redirect(url_for("index"))
