import os
from dotenv import load_dotenv

load_dotenv()

EMAIL_HOST = os.getenv("EMAIL_HOST")
EMAIL_USER = os.getenv("EMAIL_USER")
EMAIL_PASS = os.getenv("EMAIL_PASS")
EMAIL_RECIPIENT = os.getenv("EMAIL_RECIPIENT")
APPROVED_SENDER = os.getenv("APPROVED_SENDER")

GIT_REPO = os.getenv("GIT_REPO")
PROJECT_PATH = os.getenv("PROJECT_PATH")
CONTENT_PATH = os.getenv("CONTENT_PATH")

USER = os.getenv("USER")
HOST = os.getenv("HOST")
WORKING_DIR = os.getenv("WORKING_DIR")
HOST_DOMAIN = os.getenv("HOST_DOMAIN")
