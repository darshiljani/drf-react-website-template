import os

APP_ENV = os.getenv("APP_ENV", "dev")


def load_settings():
    return f"server.settings.{APP_ENV}"
