import os


def load_settings():
    env = os.getenv("APP_ENV", "dev")
    return f"server.settings.{env}"
