import logging
import os

os.environ.setdefault("DEBUG_TOOLBAR_ENABLED", "False")

from .base import *  # noqa

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

logger.debug("Test settings loaded.")

DJANGO_ALLOW_ASYNC_UNSAFE = True

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": ":memory:",
    }
}


# CELERY_TASK_ALWAYS_EAGER = True
# CELERY_TASK_EAGER_PROPAGATES = True
