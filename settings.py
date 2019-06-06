import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), ".env")
load_dotenv(dotenv_path)

DB_NAME = os.environ.get("DB_NAME")
DB_SERVER = os.environ.get("DB_SERVER")
DB_USER = os.environ.get("DB_USER")
DB_PASSWORD = os.environ.get("DB_PASSWORD")
DB_DRIVER = os.environ.get("DB_DRIVER")
