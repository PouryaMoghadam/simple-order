import os

CORS_ALLOW_METHODS = ["GET", "POST", "PUT", "PATCH", "DELETE", "OPTIONS"]

CORS_ALLOW_HEADERS = [
    "accept",
    "accept-encoding",
    "authorization",
    "content-type",
    "dnt",
    "origin",
    "user-agent",
    "x-csrftoken",
    "x-requested-with",
]

CORS_ALLOW_CREDENTIALS = True
CORS_ALLOW_ALL_ORIGINS = True

BASE_BACKEND_URL = os.environ.get("DJANGO_BASE_BACKEND_URL", default="http://localhost:8001")
BASE_FRONTEND_URL = os.environ.get("DJANGO_BASE_FRONTEND_URL", default="http://localhost:3000")
CORS_ALLOWED_ORIGINS = os.environ.get("DJANGO_CORS_ORIGIN_WHITELIST", default=[BASE_FRONTEND_URL])
