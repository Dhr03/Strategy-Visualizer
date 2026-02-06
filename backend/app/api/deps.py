from functools import lru_cache

from app.core.config import AppSettings, get_settings


@lru_cache()
def get_app_settings() -> AppSettings:
    """
    Dependency to provide application settings.
    """
    return get_settings()

