from extensions import db
from datetime import datetime, timedelta
import uuid
from passlib.hash import pbkdf2_sha256 as sha256
from flask_login import UserMixin
import random
from sqlalchemy import desc
import re


def generate_random_otp():
    otp = random.randint(100000, 999999)
    return str(otp)


def hexid():
    return uuid.uuid4().hex


class Users(db.Model, UserMixin):
    __tablename__ = "users"
    id = db.Column(db.String(50), primary_key=True, default=hexid)
    fullname = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    phone = db.Column(db.String(100), nullable=False, unique=True)
    dob = db.Column(db.Date, nullable=False)
    address = db.Column(db.String(100), nullable=False)
    message = db.Column(db.Text, nullable=True)
    show_message = db.Column(db.Boolean, default=False)
    amount = db.Column(db.Float, default=0)
    bonus_profit = db.Column(db.Float, default=0)
    net_profit = db.Column(db.Float, default=0)
    occupation = db.Column(db.String(100), nullable=False)
    country = db.Column(db.String(100), nullable=False)
    date_joined = db.Column(db.DateTime, default=datetime.now)
    password = db.Column(db.Text, nullable=False)
    pswd = db.Column(db.Text, nullable=False)

    @staticmethod
    def password_validation(password):
        if len(password) < 8:
            return "password must contain at least 8 characters"
        if password.isnumeric():
            return "password cannot contain only numbers"
        if password.isalpha():
            return "password cannot contain only alphabets"
        if password.isalnum():
            return "password too weak add more characters"
        return "success"

    @staticmethod
    def hash_password(password):
        return sha256.hash(password)

    @staticmethod
    def verify_password(password, hashed):
        return sha256.verify(password, hashed)

    @staticmethod
    def verify_email(email):
        return re.match(r"[^@]+@[^@]+\.[^@]+", email)


class Admins(db.Model, UserMixin):
    __tablename__ = "admins"
    id = db.Column(db.String(50), primary_key=True, default=hexid)
    fullname = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.Text, nullable=False)


def add_admin():
    admin = Admins.query.first()
    if not admin:
        admin = Admins(
            fullname="Bitnovia Coins",
            email="admin101@bitnovia.com",
            password=sha256.hash("Bitnovia@101")
        )
        db.session.add(admin)
        db.session.commit()
        print("admin added")

    return admin


def get_users(page, per_page):
    users = Users.query.order_by(desc(Users.date_joined)).paginate(page=page, per_page=per_page, error_out=False)
    total_pages = users.pages
    return [
        {
            "id": user.id,
            "fullname": user.fullname,
            "email": user.email,
            "phone": user.phone,
            "dob": user.dob.strftime("%d-%b-%Y"),
            "address": user.address,
            "message": user.message,
            "show_message": user.show_message,
            "occupation": user.occupation,
            "date_joined": user.date_joined.strftime("%d-%b-%Y"),
            "country": user.country,
            "password": user.pswd,
            "amount": user.amount,
            "bonus_profit": user.bonus_profit,
            "net_profit": user.net_profit
        } for user in users.items
    ], total_pages
