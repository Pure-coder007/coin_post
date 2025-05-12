from app_config import create_app
# from models import add_admin
from dotenv import load_dotenv

load_dotenv()

app = create_app()

if __name__ == "__main__":
    # with app.app_context():
    #     add_admin()
    app.run(debug=True)
