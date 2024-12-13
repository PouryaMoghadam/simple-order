"""
Django settings for fiblodex-service project.

Generated by 'django-admin startproject' using Django 5.0.2.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

import os

import dotenv
from django.utils import timezone

BASE_DIR = os.getcwd()
APPS_DIR = BASE_DIR + "/src"

dotenv.load_dotenv(BASE_DIR + "/.env")

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

SECRET_KEY = os.environ.get("SECRET_KEY", default="thisisbasekey")
DEBUG = os.environ.get("DEBUG", default=True)
ALLOWED_HOSTS = ["*"]


# Application definition
LOCAL_APPS = [
    # "src.core.apps.CoreConfig",
    # "src.user.apps.UserConfig",
    # "src.wallet.apps.WalletConfig",
    # "src.order.apps.OrderConfig",
]

THIRD_PARTY_APPS = [
    "django_celery_results",
    "django_celery_beat",
    "corsheaders",
    "django_jalali",
]

INSTALLED_APPS = [
    # "admin_two_factor.apps.TwoStepVerificationConfig",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # we need add static files serve apps here
    *THIRD_PARTY_APPS,
    *LOCAL_APPS,
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "config.urls"
ASGI_APPLICATION = "config.asgi.application"
TIME_ZONE_APP = os.environ.get("TIME_ZONE_APP", default="UTC")

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
            ],
        },
    },
]

# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASE_CONFIG = {
    "ENGINE": "django.db.backends.postgresql",
    "NAME": os.environ.get("POSTGRES_DB"),
    "USER": os.environ.get("POSTGRES_USER"),
    "PASSWORD": os.environ.get("POSTGRES_PASSWORD"),
    "HOST": os.environ.get("POSTGRES_HOST"),
    "PORT": os.environ.get("POSTGRES_PORT"),
    "OPTIONS": {
        "options": f"-c timezone={TIME_ZONE_APP}",  # Set the database time zone
    },
}


DATABASES = {"default": DATABASE_CONFIG}


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = TIME_ZONE_APP

USE_I18N = True

USE_TZ = True


timezone.activate(TIME_ZONE)


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR, "static")
STATIC_URL = "static/"

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


# Read Redis configuration from environment variables
REDIS_HOST = os.environ.get("REDIS_HOST", default="127.0.0.1")
REDIS_PORT = os.environ.get("REDIS_PORT", default="6379")
REDIS_CACHE_DB = os.environ.get("REDIS_CACHE_DB", default="2")
REDIS_PASSWORD = os.environ.get("REDIS_PASSWORD")


CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": f"redis://{REDIS_HOST}:{REDIS_PORT}/{REDIS_CACHE_DB}",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
            "PASSWORD": REDIS_PASSWORD,
        },
    }
}

from config.settings.celery import *  # noqa
from config.settings.cors import *  # noqa
from config.settings.logging import *  # noqa