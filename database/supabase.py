from pathlib import Path
from dotenv import load_dotenv
from supabase import create_client
import os

# Cari file .env secara eksplisit
BASE_DIR = Path(__file__).resolve().parent.parent
ENV_PATH = BASE_DIR / ".env"

print("BASE_DIR :", BASE_DIR)
print("ENV_PATH :", ENV_PATH)
print("ENV EXISTS :", ENV_PATH.exists())

load_dotenv(dotenv_path=ENV_PATH)

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

print("URL :", SUPABASE_URL)
print("KEY FOUND :", SUPABASE_KEY is not None)

supabase = create_client(
    SUPABASE_URL,
    SUPABASE_KEY
)