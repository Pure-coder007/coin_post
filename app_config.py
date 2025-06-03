from extensions import db, login_manager, migrate
from flask import redirect, flash, url_for, session, render_template, Flask, request
from view_functions import AuthenticationBlueprint, UserBlueprint, AdminBlueprint
from models import Users, Admins, add_admin
from datetime import timedelta
import os
from dotenv import load_dotenv
import logging
from sqlalchemy.exc import OperationalError
from flask_migrate import Migrate

load_dotenv()

# Configure logging
logging.basicConfig()
logging.getLogger('sqlalchemy.engine').setLevel(logging.WARNING)

def get_database_uri():
    """Get database URI with proper PostgreSQL formatting and fallbacks"""
    # Default PostgreSQL configuration
    default_uri = "mysql+pymysql://{user}:{password}@{host}/{dbname}".format(
        user="novi",
        password="novi",
        host="localhost",
        dbname="novi"
    )
    
    uri = os.getenv("DATABASE_URI", default_uri)
    
    return uri

def create_app():
    app = Flask(__name__)
    
    # Configuration
    app.config.update(
        SQLALCHEMY_DATABASE_URI=get_database_uri(),
        SQLALCHEMY_TRACK_MODIFICATIONS=False,
        SECRET_KEY=os.getenv("SECRET_KEY", "default_secret_key"),
        DEBUG=False,
        PERMANENT_SESSION_LIFETIME=timedelta(days=7))
    
    # Initialize extensions
    db.init_app(app)
    login_manager.init_app(app)
    
    # Initialize Flask-Migrate AFTER db.init_app()
    migrate = Migrate(app, db)  # This replaces migrate.init_app(app, db)

    # with app.app_context():
    #     add_admin()
    
    # User loader
    @login_manager.user_loader
    def load_user(id):
        """Load user from either Users or Admins table"""
        return Users.query.get(id) or Admins.query.get(id)

    # Error handlers
    @app.errorhandler(404)
    def page_not_found(e):
        return render_template("404.html"), 404

    @app.errorhandler(401)
    def unauthorized(e):
        session["alert"] = "Login to access this page"
        session["bg_color"] = "danger"
        return redirect(url_for("auth.login"))

    # Before request setup
    @app.before_request
    def before_request():
        session.permanent = True
        session["referral"] = request.referrer

    # Register blueprints
    app.register_blueprint(AuthenticationBlueprint)
    app.register_blueprint(UserBlueprint)
    app.register_blueprint(AdminBlueprint)

    # Database initialization with error handling
    with app.app_context():
        try:
            # Only create tables if they don't exist
            # In production, you should use migrations instead
            if os.getenv("FLASK_ENV") == "development":
                db.create_all()
                app.logger.info("Database tables created/verified")
        except OperationalError as e:
            app.logger.error(f"Database connection failed: {str(e)}")
            # You might want to add fallback behavior here
        except Exception as e:
            app.logger.error(f"Database initialization error: {str(e)}")

    return app