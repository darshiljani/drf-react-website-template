from .base import *  # NoQA : F403

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "verbose": {
            "format": "{levelname} - {asctime} | P : {process:d}, T : {thread:d} | {module} : {message}",
            "style": "{",
        },
        "simple": {
            "format": "{levelname} - {asctime} | {module} : {message}",
            "style": "{",
        },
    },
    "handlers": {
        "console": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "formatter": "simple",
        },
    },
    "loggers": {
        "django": {"handlers": ["console"], "propogate": True, "level": "INFO"}
    },
}
