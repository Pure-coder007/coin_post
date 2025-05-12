from flask import Flask, render_template, request, redirect, url_for, flash, session

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html')


@app.route('/about', methods=['GET', 'POST'])
def about():
    return render_template('about.html')


@app.route('/bitcoin_chart', methods=['GET', 'POST'])
def bitcoin_chart():
    return render_template('bitcoin_chart.html')


@app.route('/blog', methods=['GET', 'POST'])
def blog():
    return render_template('blog.html')


@app.route('/faq', methods=['GET', 'POST'])
def faq():
    return render_template('faq.html')


@app.route('/investment_plan', methods=['GET', 'POST'])
def investment_plan():
    return render_template('investment_plan.html')


@app.route('/server_error_page', methods=['GET', 'POST'])
def server_error_page():
    return render_template('server_error_page.html')


@app.route('/service', methods=['GET', 'POST'])
def service():
    return render_template('service.html')


@app.route('/sign_up', methods=['GET', 'POST'])
def sign_up():
    return render_template('sign_up.html')


@app.route('/team', methods=['GET', 'POST'])
def team():
    return render_template('team.html')


@app.route('/terms_of_service', methods=['GET', 'POST'])
def terms_of_service():
    return render_template('terms_of_service.html')


@app.route('/error_404', methods=['GET', 'POST'])
def error_404():
    return render_template('error_404.html')


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    return render_template('contact.html')


@app.route('/reset_password', methods=['GET', 'POST'])
def reset_password():
    return render_template('reset_password.html')


@app.route('/user', methods=['GET', 'POST'])
def user():
    return render_template('user.html')


@app.route('/add_funds', methods=['GET', 'POST'])
def add_funds():
    return render_template('add_funds.html')


@app.route('/profile_page', methods=['GET', 'POST'])
def profile_page():
    return render_template('profile_page.html')


@app.route('/update_mobile', methods=['GET', 'POST'])
def update_mobile():
    return render_template('update_mobile.html')


@app.route('/withdrawal', methods=['GET', 'POST'])
def withdrawal():
    return render_template('withdrawal.html')


@app.route('/account', methods=['GET', 'POST'])
def account():
    return render_template('account.html')



# @app.route('/bitcoin_chart', methods=['GET', 'POST'])
# def bitcoin_chart():
#     return render_template('bitcoin_chart.html')


if __name__ == '__main__':
    app.run(debug=True)
