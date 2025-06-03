import os

# ✅ TMPDIR fix
tmp_path = os.path.join(os.path.dirname(__file__), 'tmp')
os.makedirs(tmp_path, exist_ok=True)
os.environ['TMPDIR'] = tmp_path
os.environ['TEMP'] = tmp_path
os.environ['TMP'] = tmp_path

import tempfile
tempfile.tempdir = tmp_path

# ✅ Load Flask app
from app_config import create_app

application = create_app()

