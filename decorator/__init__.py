from models import Users, Admins
from flask_login import current_user
from flask import url_for, redirect, session, request
from functools import wraps


# decorator admin required
def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not Admins.query.get(current_user.id):
            session["alert"] = "You cannot access this page"
            session["bg_color"] = "danger"
            return redirect(url_for('users.index'))
        return f(*args, **kwargs)
    return decorated_function


# user decorator
def user_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not Users.query.get(current_user.id):
            session["alert"] = "You cannot access this page"
            session["bg_color"] = "danger"
            return redirect(url_for('users.index'))
        return f(*args, **kwargs)
    return decorated_function


# check if logged in
def check_logged_in(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if current_user.is_authenticated:
            if Admins.query.get(current_user.id):
                session["alert"] = "You cannot access this page"
                session["bg_color"] = "info"
                return redirect(url_for('admin.admin'))
            if Users.query.get(current_user.id):
                session["alert"] = "You cannot access this page"
                session["bg_color"] = "info"
                return redirect(url_for('users.user_dash'))
            previous_endpoint = session.get("referral")
            print(previous_endpoint, "previous endpoint")
            return redirect(previous_endpoint)
        return f(*args, **kwargs)
    return decorated_function
