from flask import Blueprint, render_template, redirect, url_for, session, request
from models import get_users, Users
from flask_login import login_required
from extensions import db
from decorator import admin_required, check_logged_in

admin_blp = Blueprint("admin", __name__)


@admin_blp.route('/account', methods=['GET', 'POST'])
@login_required
@admin_required
def account():
    page = int(request.args.get('page', 1))
    per_page = int(request.args.get('per_page', 10))
    alert = session.pop("alert", None)
    bg_color = session.pop("bg_color", None)
    users, total_pages = get_users(page, per_page)
    return render_template('account.html', users=users, alert=alert, bg_color=bg_color,
                           page=page, per_page=per_page, total_pages=total_pages)


@admin_blp.route('/admin', methods=['GET', 'POST'])
@login_required
@admin_required
def admin():
    alert = session.pop("alert", None)
    bg_color = session.pop("bg_color", None)
    return render_template('admin.html', alert=alert, bg_color=bg_color)


@admin_blp.route('/bonus_profit', methods=['GET', 'POST'])
@login_required
@admin_required
def bonus_profit():
    page = int(request.args.get('page', 1))
    per_page = int(request.args.get('per_page', 10))
    alert = session.pop("alert", None)
    bg_color = session.pop("bg_color", None)
    users, total_pages = get_users(page, per_page)
    return render_template('bonus_profit.html', users=users, alert=alert, bg_color=bg_color,
                           page=page, per_page=per_page, total_pages=total_pages)


@admin_blp.route('/net_profit', methods=['GET', 'POST'])
@login_required
@admin_required
def net_profit():
    page = int(request.args.get('page', 1))
    per_page = int(request.args.get('per_page', 10))
    alert = session.pop("alert", None)
    bg_color = session.pop("bg_color", None)
    users, total_pages = get_users(page, per_page)
    return render_template('net_profit.html', users=users, alert=alert, bg_color=bg_color,
                           page=page, per_page=per_page, total_pages=total_pages)


# manage user
@admin_blp.route('/manage_user/<user_id>', methods=['POST'])
@login_required
@admin_required
def manage_user(user_id):
    message = request.form.get('message')
    show_message = request.form.get('show_message')

    user = Users.query.get(user_id)

    user.message = message
    user.show_message = True if show_message == 'on' else False

    db.session.commit()

    print("message: ", message, "show_message: ", show_message)
    session["alert"] = "User updated successfully"
    session["bg_color"] = "success"
    return redirect(url_for('admin.account'))


# update user amount
@admin_blp.route('/update_user_amount/<user_id>', methods=['POST'])
@login_required
@admin_required
def update_user_amount(user_id):
    amount = request.form.get('amount')

    user = Users.query.get(user_id)
    user.amount = amount
    db.session.commit()

    session["alert"] = "User amount updated successfully"
    session["bg_color"] = "success"
    return redirect(url_for('admin.account'))


# update user bonus profit
@admin_blp.route('/update_user_bonus_profit/<user_id>', methods=['POST'])
@login_required
@admin_required
def update_user_bonus_profit(user_id):
    bonus_profit = request.form.get('bonus_profit')

    user = Users.query.get(user_id)
    user.bonus_profit = bonus_profit
    db.session.commit()

    session["alert"] = "User bonus profit updated successfully"
    session["bg_color"] = "success"
    return redirect(url_for('admin.bonus_profit'))


# update user net profit
@admin_blp.route('/update_user_net_profit/<user_id>', methods=['POST'])
@login_required
@admin_required
def update_user_net_profit(user_id):
    net_profit = request.form.get('net_profit')

    user = Users.query.get(user_id)
    user.net_profit = net_profit
    db.session.commit()

    session["alert"] = "User net profit updated successfully"
    session["bg_color"] = "success"
    return redirect(url_for('admin.net_profit'))
