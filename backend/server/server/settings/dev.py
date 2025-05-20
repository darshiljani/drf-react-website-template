from .base import *  # NoQA : F403

ALLOWED_HOSTS = ["*"]
DEV_APPS = ["drf_yasg"]
INSTALLED_APPS = INSTALLED_APPS + DEV_APPS  # NoQA: F405

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.postgresql",
#         "NAME": "db_name",
#         "USER": "postgres",
#         "PASSWORD": "db_pwd",
#         "HOST": "127.0.0.1",
#         "PORT": "5432",
#     }
# }

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": "db.sqlite3",
    }
}

# Swagger documentation
SWAGGER_SETTINGS = {
    "DOC_EXPANSION": "list",
    "APIS_SORTER": "alpha",
    "USE_SESSION_AUTH": False,
    "SECURITY_DEFINITIONS": {
        "Bearer": {  # <<-- is for JWT access token
            "type": "apiKey",
            "name": "Authorization",
            "in": "header",
        }
    },
}


CORS_ALLOWED_ORIGINS = [
    "http://localhost:5500",  # Live Server
    "http://localhost:3000",  # Create React App 1
    "http://localhost:3001",  # Create React App 1
    "http://localhost:5173",  # Vite
    "http://localhost:5174",  # Vite 2
]

INTERNAL_IPS = ["http://127.0.0.1"]

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
