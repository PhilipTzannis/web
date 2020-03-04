"""
Django settings for academy project.

Generated by 'django-admin startproject' using Django 2.2.2.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os

from dotenv import load_dotenv

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.humanize",
    "django_extensions",
    "debug_toolbar",
    "constance",
    "constance.backends.database",
    "rest_framework",
    "rest_framework.authtoken",
    "bootstrap4",
    "django_celery_beat",
    "svelte",
    "games",
    "web",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "debug_toolbar.middleware.DebugToolbarMiddleware",
    "academy.cors.CorsMiddleware",
]

ROOT_URLCONF = "academy.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "constance.context_processors.config",
                "academy.context_processors.constants",
                "games.context_processors.seasons",
            ]
        },
    }
]

WSGI_APPLICATION = "academy.wsgi.application"


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
    }
}

# Password storage
# https://docs.djangoproject.com/en/2.2/topics/auth/passwords/#auth-password-storage

PASSWORD_HASHERS = [
    # Default
    "django.contrib.auth.hashers.PBKDF2PasswordHasher",
    "django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher",
    "django.contrib.auth.hashers.Argon2PasswordHasher",
    "django.contrib.auth.hashers.BCryptSHA256PasswordHasher",
    # Added for supporting passwords from old site
    "django.contrib.auth.hashers.BCryptPasswordHasher",
]

# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

# Disable all validators, we want to support "test"
AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "academy.password_validators.StrongAdminPasswordValidator"}
]


# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "Europe/Copenhagen"

USE_I18N = True

USE_L10N = True

USE_TZ = True

# 64 MB
DATA_UPLOAD_MAX_MEMORY_SIZE = 64 * 1024 ** 2

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = "/static/"
STATIC_ROOT = os.path.join(BASE_DIR, "static/")

MEDIA_URL = "/media/"
MEDIA_ROOT = "media"

LOGIN_URL = "/login/"
LOGIN_REDIRECT_URL = "/"
LOGOUT_REDIRECT_URL = "/"

AUTH_USER_MODEL = "games.User"

REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly"
    ],
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework.authentication.SessionAuthentication",
        "rest_framework.authentication.TokenAuthentication",
    ],
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.LimitOffsetPagination",
    "DEFAULT_FILTER_BACKENDS": ("django_filters.rest_framework.DjangoFilterBackend",),
    "PAGE_SIZE": 100,
}

DEBUG_TOOLBAR_CONFIG = {"SHOW_TOOLBAR_CALLBACK": "academy.debug_toolbar.show_toolbar"}

CONSTANCE_BACKEND = "constance.backends.database.DatabaseBackend"
CONSTANCE_CONFIG = {
    "BANNER_ENABLED": (False, "Show banner", bool),
    "BANNER_TEXT": ("", "Banner text", str),
    "BANNER_URL": ("https://dropdu.nu/", "Banner URL", str),
    "BANNER_COLOR": ("#0094c4", "Banner color", str),
    "BANNER_BLINK": (False, "Should banner text blink?", bool),
}


load_dotenv()
