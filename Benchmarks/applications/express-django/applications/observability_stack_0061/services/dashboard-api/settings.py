import os

SECRET_KEY = os.environ.get("APP_SECRET_KEY") or os.urandom(32).hex()
DEBUG = False
ALLOWED_HOSTS = ["*"]
ROOT_URLCONF = "urls"
INSTALLED_APPS = []
MIDDLEWARE = ["django.contrib.sessions.middleware.SessionMiddleware"]
SESSION_ENGINE = "django.contrib.sessions.backends.signed_cookies"
DATABASES = {"default": {"ENGINE": "django.db.backends.sqlite3", "NAME": os.environ.get("DATABASE_PATH", "app.db")}}
TEMPLATES = [{"BACKEND": "django.template.backends.django.DjangoTemplates", "DIRS": [], "APP_DIRS": False, "OPTIONS": {}}]
