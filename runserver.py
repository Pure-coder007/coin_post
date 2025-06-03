# runserver.py

import os

# ✅ TMPDIR fix for cPanel temporary directory issue
tmp_path = os.path.join(os.path.dirname(__file__), 'tmp')
os.makedirs(tmp_path, exist_ok=True)  # make sure the folder exists
os.environ['TMPDIR'] = tmp_path
os.environ['TEMP'] = tmp_path
os.environ['TMP'] = tmp_path

import tempfile
tempfile.tempdir = tmp_path

# 👇 Now you can safely import the rest
from app_config import create_app
from dotenv import load_dotenv

load_dotenv()

app = create_app()

if __name__ == "__main__":
    app.run(debug=False, host='0.0.0.0', port=8000)
