from flask import render_template, request, redirect, url_for, session
from app import IssueTracker
from app.tools import validate
from app.tools.dbTools import DataBaseManager
from app.tools.hashTools import Hash
from app.tools.faceUnlock import FaceUnlock


@IssueTracker.route('/newuser')
def create_user_landing():
    if 'authorized' in session and session['authorized'] is True:
        return redirect(url_for("render_gallery"))

    return render_template("newuser.html", username=None,  first_name=None, last_name=None,
                           email=None, password=None, password_conf=None)


@IssueTracker.route('/newuser/create', methods=['POST'])
def create_user():
    if 'authorized' in session and session['authorized'] is True:
        return redirect(url_for("render_gallery"))

    input_username = request.form.get("var1")
    input_first_name = request.form.get("var2")
    input_last_name = request.form.get("var3")
    input_email = request.form.get("var4")
    input_password = request.form.get("var5")
    input_password_conf = request.form.get("var6")
    picture = request.form.get('var7')

    field = validate.regex()
    username = field.validate(field.user_name_pattern, input_username)
    first_name = field.validate(field.first_name_pattern, input_first_name)
    last_name = field.validate(field.last_name_pattern, input_last_name)
    email = field.validate(field.email_pattern, input_email)
    password = field.validate(field.password_pattern, input_password)
    password_conf = password == input_password_conf

    err_msg = compose_error_message(username, first_name, last_name, email, password, password_conf)

    if err_msg is not None:
        return render_template("newuser.html", error=err_msg, username=input_username, first_name=input_first_name,
                               last_name=input_last_name, email=input_email, password=input_password,
                               password_conf=input_password_conf)

    pwd_manager = Hash()
    salt, hashpwd = pwd_manager.get_salt_hash(password)
    stored_pwd = "$" + salt + "$" + hashpwd.decode("utf-8")

    email_already_registered = DataBaseManager.email_already_exists(email)

    if not email_already_registered:
        # Add
        db_success = DataBaseManager.add_user(username, first_name, last_name, email, stored_pwd)
        user = input_username + '_master'
        FaceUnlock.upload_s3(picture, user)

        if db_success:
            session['user'] = username
            session['authorized'] = True

            return redirect(url_for('render_main_issue_list'))
        else:
            # Getting here means that either there was a database  error or the username is already taken.
            # Since the user will have to retry anyways, we might as well say there was an error with the
            # chosen username
            err_msg = ["Username is unavailable."]
            return render_template("newuser.html", error=err_msg, username=input_username, first_name=input_first_name,
                                   last_name=input_last_name, email=input_email, password=input_password,
                                   password_conf=input_password_conf)
    else:
        err_msg = ["An account already exists with this Email"]
        return render_template("newuser.html", error=err_msg, username=username, first_name=first_name,
                               last_name=last_name, email=email, password=password, password_conf=password_conf)


def compose_error_message(username, first_name, last_name, email, password, password_conf):
    err_msg = []

    if not username:
        err_msg.append("Invalid username.")

    if not first_name:
        err_msg.append("Invalid first name.")

    if not last_name:
        err_msg.append("Invalid last name.")

    if not email:
        err_msg.append("Invalid email.")

    if not password:
        err_msg.append("Invalid password.")

    if not password_conf:
        err_msg.append("Password and verification do not match.")

    if len(err_msg) > 0:
        err_msg.append("Please hover your cursor over the fields below to check their requirements.")
    else:
        err_msg = None

    return err_msg
