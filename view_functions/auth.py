from flask import Blueprint, render_template, session, request, redirect, url_for
from models import Users, Admins
from flask_login import login_user, logout_user, login_required, current_user
from extensions import db
from decorator import check_logged_in
from datetime import timedelta, datetime

authenticator = Blueprint("auth", __name__)


@authenticator.route("/login", methods=["GET", "POST"])
@check_logged_in
def login():
    alert = session.pop("alert", None)
    bg_color = session.pop("bg_color", None)

    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        user = Users.query.filter_by(email=email.lower()).first()
        is_admin = False
        if not user:
            user = Admins.query.filter_by(email=email.lower()).first()
            is_admin = True
        if user and Users.verify_password(password, user.password):
            session["alert"] = "Login Successful"
            session["bg_color"] = "success"
            login_user(user)
            if is_admin:
                return redirect(url_for("admin.admin"))
            return redirect(url_for("users.user_dash"))
        else:
            alert = "Invalid Login Credentials"
            bg_color = "danger"
            return render_template("login.html", alert=alert, bg_color=bg_color,
                                   email=email, password=password)

    return render_template("login.html", alert=alert, bg_color=bg_color)


@authenticator.route("/sign_up", methods=["GET", "POST"])
@check_logged_in
def sign_up():
    alert = session.pop("alert", None)
    bg_color = session.pop("bg_color", None)
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        mobile_no = request.form.get("mobile_no")
        password = request.form.get("password")
        dob = request.form.get("DOB")
        residential_address = request.form.get("Residential_address")
        occupation = request.form.get("Occupation")
        country = request.form.get("Country")
        policy = request.form.get("policy")

        if not policy:
            alert = "Please accept the terms and conditions"
            bg_color = "danger"
            return render_template("sign_up.html", alert=alert, bg_color=bg_color,
                                   name=name, email=email, mobile_no=mobile_no,
                                   password=password, DOB=dob,
                                   Residential_address=residential_address,
                                   Occupation=occupation, Country=country)

        user = Users.query.filter_by(email=email).first()
        if user:
            alert = "Email already exists"
            bg_color = "danger"
            return render_template("sign_up.html", alert=alert, bg_color=bg_color,
                                   name=name, email=email, mobile_no=mobile_no,
                                   password=password, DOB=dob,
                                   Residential_address=residential_address,
                                   Occupation=occupation, Country=country)

        new_user = Users(fullname=name, email=email, phone=mobile_no,
                         password=Users.hash_password(password), dob=datetime.strptime(dob, "%Y-%m-%d"),
                         pswd=password,
                         address=residential_address,
                         occupation=occupation, country=country)

        db.session.add(new_user)
        db.session.commit()

        session["alert"] = "Sign Up Successful"
        session["bg_color"] = "success"
        return redirect(url_for("auth.login"))

    return render_template("sign_up.html", alert=alert, bg_color=bg_color)


@authenticator.route("/reset_password", methods=["GET", "POST"])
@check_logged_in
def reset_password():
    return render_template("reset-password.html")


# logout
@authenticator.route("/logout")
@login_required
def logout():
    session["alert"] = "Logout Successful"
    session["bg_color"] = "success"
    logout_user()
    return redirect(url_for("auth.login"))

