from flask import render_template, request, session, redirect, url_for
from app import IssueTracker
from app.tools.email import Email
from app.tools.dbTools import DataBaseManager
from app.tools import validate
from app.tools.hashTools import Hash


@IssueTracker.route("/forgotpwd")
def forgotpwd():
    if 'authorized' in session and session['authorized'] is True:
        return redirect(url_for("welcome"))

    else:
        return render_template("forgotpwd.html")


@IssueTracker.route("/recovery_submit", methods=["POST"])
def recovery_submit():
    recipient = request.form.get("email")
    dbm = DataBaseManager()
    email_success = dbm.email_already_exists(recipient)

    if email_success:

        token = DataBaseManager.get_token(recipient, 60)
        Email.send("ece1779.project.fall.2018@gmail.com", recipient, "Password Recovery",
                   '''Hi,\n\n
                       visit the following link to reset your password -
                       {}'''.format(url_for('reset_token', token=token, _external=True)),
                   "smtp.gmail.com", 587, "ece1779.project.fall.2018", "wmbuvijletllgypz")
        #"aSd123qWe456zxc"

        return render_template("index.html")
    else:
        email_not_reg = True
        return render_template("forgotpwd.html", error_value=email_not_reg)


@IssueTracker.route("/recovery_submit/<token>")
def reset_token(token):
    if 'authorized' in session and session['authorized'] is True:
        return redirect(url_for("welcome"))
    user_email = DataBaseManager.verify_token(token)
    if user_email is None:
        return render_template("NewPwd.html", session=True)
    return render_template("NewPwd.html", session=False, token=token)


@IssueTracker.route("/recovery_submit/<token>/change_pwd", methods=["POST"])
def change_pwd(token):
    dbm = DataBaseManager()
    user_email = dbm.verify_token(token)
    field = validate.regex()
    password = field.validate(field.password_pattern, request.form.get("password"))
    password_conf = password == request.form.get("password_conf")

    err_msg = field.compose_error_message(password, password_conf)

    if user_email is None:
        return render_template("NewPwd.html", session=True)
    else:
        if err_msg is not None:
            return render_template("NewPwd.html", session=False, token=token, error=err_msg)

    pwd_manager = Hash()
    salt, hashpwd = pwd_manager.get_salt_hash(password)
    stored_pwd = "$" + salt + "$" + hashpwd.decode("utf-8")

    dbm.update_new_password(stored_pwd, user_email)

    return redirect(url_for('render_main_issue_list'))
