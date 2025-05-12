import psycopg2  # Install with: pip install psycopg2-binary
from dotenv import load_dotenv
import os
from pathlib import Path

# Load .env
env_path = Path(__file__).parent / '.env'
load_dotenv(dotenv_path=env_path)

config = {
    'host': os.getenv('DB_HOST'),
    'user': os.getenv('DB_USER'),
    'password': os.getenv('DB_PASSWORD'),
    'dbname': os.getenv('DB_NAME'),
    'port': int(os.getenv('DB_PORT', 5432)),
}

try:
    connection = psycopg2.connect(**config)
    print("✅ PostgreSQL connection successful!")
    connection.close()
except Exception as e:
    print("❌ PostgreSQL connection failed:", e)