import os

from django.utils.timezone import get_default_timezone_name

REDIS_HOST = os.environ.get("REDIS_HOST", default="127.0.0.1")
REDIS_PORT = os.environ.get("REDIS_PORT", default="6379")
REDIS_PASSWORD = os.environ.get("REDIS_PASSWORD")

REDIS_URL = f"redis://:{REDIS_PASSWORD}@{REDIS_HOST}:{REDIS_PORT}/1"\
    if REDIS_PASSWORD else f"redis://{REDIS_HOST}:{REDIS_PORT}/1"

CELERY_BROKER_URL = REDIS_URL
CELERY_RESULT_BACKEND = "django-db"

CELERY_ACCEPT_CONTENT = ["json"]
CELERY_TASK_SERIALIZER = "json"
CELERY_RESULT_SERIALIZER = "json"
CELERY_TIMEZONE = get_default_timezone_name()
CELERY_RESULT_EXTENDED = True

CELERY_TASK_SOFT_TIME_LIMIT = 60
CELERY_TASK_TIME_LIMIT = 120

CELERY_BEAT_SCHEDULE = {
    # "debug_task": {
    #     "task": "debug_task",
    #     "schedule": timedelta(seconds=1),
    # },
    # Add more tasks as needed
    # please add task from admin panel periodic tasks management
}
