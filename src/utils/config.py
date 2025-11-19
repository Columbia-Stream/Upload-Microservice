import os
from dotenv import load_dotenv

# This function searches for and loads variables from the .env file
load_dotenv()

PROJECT_ID = os.getenv("PROJECT_ID")
# SECRET_ID = os.getenv("SECRET_ID")
FIREBASE_API_KEY = os.getenv("FIREBASE_API_KEY")
VIDEO_DOMAIN = os.getenv("VIDEO_DOMAIN")


# App Settings
APP_ENV = os.getenv("APP_ENV", "development")  # dev/staging/prod
