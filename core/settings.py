import os
from pathlib import Path
import dj_database_url
from dotenv import load_dotenv
from app.storage_backends import ImageKitMediaStorage

# Load environment variables from .env file
load_dotenv()

# --------------------------------------------------------------------------
# BASE DIRECTORY
# --------------------------------------------------------------------------
BASE_DIR = Path(__file__).resolve().parent.parent
TEMPLATES_DIR = os.path.join(BASE_DIR, "app", "templates")

# --------------------------------------------------------------------------
# SECURITY SETTINGS
# --------------------------------------------------------------------------
SECRET_KEY = os.environ.get(
    "SECRET_KEY", "django-insecure-3ko70zjdv!v7+5ailo=3rfcx_b0xv$nz60xkg=k69c=hbp2w1z"
)
DEBUG = os.environ.get("DEBUG", "True") == "True"
ALLOWED_HOSTS = ["*"]

# --------------------------------------------------------------------------
# APPLICATIONS
# --------------------------------------------------------------------------
INSTALLED_APPS = [
    "app",
    "admin_interface",
    "colorfield",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "imagekitio",  # ImageKit SDK
    "imagekitio_storage",  # ImageKit Storage Backend
]

X_FRAME_OPTIONS = "SAMEORIGIN"
SILENCED_SYSTEM_CHECKS = ["security.W019"]

# --------------------------------------------------------------------------
# MIDDLEWARE
# --------------------------------------------------------------------------
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "app.middleware.NoCacheMiddleware",
]

ROOT_URLCONF = "core.urls"

# --------------------------------------------------------------------------
# TEMPLATES
# --------------------------------------------------------------------------
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [TEMPLATES_DIR],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "core.wsgi.application"

# --------------------------------------------------------------------------
# DATABASE (PostgreSQL via dj_database_url)
# --------------------------------------------------------------------------
DATABASES = {
    "default": dj_database_url.config(
        default=os.environ.get("DATABASE_URL"),
        conn_max_age=600,
        ssl_require=True
    )
}

# --------------------------------------------------------------------------
# PASSWORD VALIDATION
# --------------------------------------------------------------------------
AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# --------------------------------------------------------------------------
# INTERNATIONALIZATION
# --------------------------------------------------------------------------
LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True

# --------------------------------------------------------------------------
# STATIC & MEDIA FILES (Whitenoise + ImageKit)
# --------------------------------------------------------------------------
STATIC_URL = "/static/"
STATICFILES_DIRS = [os.path.join(BASE_DIR, "static")]
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

# --------------------------------------------------------------------------
# IMAGEKIT.IO STORAGE CONFIGURATION
# --------------------------------------------------------------------------
IMAGEKIT_PUBLIC_KEY = os.getenv("IMAGEKIT_PUBLIC_KEY")
IMAGEKIT_PRIVATE_KEY = os.getenv("IMAGEKIT_PRIVATE_KEY")
IMAGEKIT_URL_ENDPOINT = os.getenv("IMAGEKIT_URL_ENDPOINT")

# Define ImageKit credentials
IMAGEKIT = {
    "public_key": IMAGEKIT_PUBLIC_KEY,
    "private_key": IMAGEKIT_PRIVATE_KEY,
    "url_endpoint": IMAGEKIT_URL_ENDPOINT,
}

# Use ImageKit storage for all uploaded media
# DEFAULT_FILE_STORAGE = "imagekitio_storage.storage.MediaStorage"
DEFAULT_FILE_STORAGE = "app.storage_backends.ImageKitMediaStorage"


# Serve files from ImageKit CDN
MEDIA_URL = f"{IMAGEKIT_URL_ENDPOINT}/" if IMAGEKIT_URL_ENDPOINT else "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")


# --------------------------------------------------------------------------
# AUTH & SESSION SETTINGS
# --------------------------------------------------------------------------
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
AUTH_USER_MODEL = "app.CustomUser"

LOGIN_URL = "/login/"
LOGIN_REDIRECT_URL = "/dashboard/"
LOGOUT_REDIRECT_URL = "/login/"

SESSION_EXPIRE_AT_BROWSER_CLOSE = True
SESSION_COOKIE_AGE = 1800  # 30 minutes
SESSION_SAVE_EVERY_REQUEST = True

# --------------------------------------------------------------------------
# EMAIL CONFIGURATION
# --------------------------------------------------------------------------
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "smtp.gmail.com"
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = "newmahavirtent@gmail.com"
EMAIL_HOST_PASSWORD = "xnpv yhyc mjfv rkvt"
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
