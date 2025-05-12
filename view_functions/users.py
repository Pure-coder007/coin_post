from flask import Blueprint, render_template, session
from flask_login import login_required, current_user
from decorator import user_required, check_logged_in

user = Blueprint("users", __name__)


@user.route('/')
@check_logged_in
def index():
    return render_template('index.html')


@user.route('/about', methods=['GET', 'POST'])
@check_logged_in
def about():
    return render_template('about.html')


@user.route('/bitcoin_chart', methods=['GET', 'POST'])
@check_logged_in
def bitcoin_chart():
    return render_template('bitcoin_chart.html')


@user.route('/user', methods=['GET', 'POST'])
@login_required
@user_required
def user_dash():
    alert = session.pop("alert", None)
    bg_color = session.pop("bg_color", None)
    return render_template('user.html', alert=alert, bg_color=bg_color)


@user.route('/blog', methods=['GET', 'POST'])
@check_logged_in
def blog():
    return render_template('blog.html')


@user.route('/faq', methods=['GET', 'POST'])
@check_logged_in
def faq():
    return render_template('faq.html')


@user.route('/investment_plan', methods=['GET', 'POST'])
@check_logged_in
def investment_plan():
    return render_template('investment_plan.html')


@user.route('/server_error_page', methods=['GET', 'POST'])
@check_logged_in
def server_error_page():
    return render_template('server_error_page.html')


@user.route('/service', methods=['GET', 'POST'])
@check_logged_in
def service():
    return render_template('service.html')


@user.route('/team', methods=['GET', 'POST'])
@check_logged_in
def team():
    return render_template('team.html')


@user.route('/terms_of_service', methods=['GET', 'POST'])
@check_logged_in
def terms_of_service():
    return render_template('terms_of_service.html')


@user.route('/error_404', methods=['GET', 'POST'])
def error_404():
    return render_template('error_404.html')


@user.route('/contact', methods=['GET', 'POST'])
@check_logged_in
def contact():
    return render_template('contact.html')


@user.route('/add_funds', methods=['GET', 'POST'])
@login_required
@user_required
def add_funds():
    return render_template('add_funds.html')


@user.route('/withdrawal', methods=['GET', 'POST'])
@login_required
@user_required
def withdrawal():
    return render_template('withdrawal.html')


@user.route('/profile_page', methods=['GET', 'POST'])
def profile_page():
    return render_template('profile_page.html')


@user.route('/update_mobile', methods=['GET', 'POST'])
def update_mobile():
    return render_template('update_mobile.html')


@user.route('/layout', methods=['GET', 'POST'])
def layout():
    return render_template('layout.html')
