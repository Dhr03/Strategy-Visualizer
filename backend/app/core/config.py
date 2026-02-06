from functools import lru_cache
from typing import Optional

from pydantic import BaseSettings, Field


class AppSettings(BaseSettings):
    """
    Central application configuration.

    Reads from environment variables and an optional `.env` file.
    """

    app_name: str = Field("Strategy Visualizer API", env="APP_NAME")
    debug: bool = Field(False, env="DEBUG")

    # FastF1 / strategy-related settings
    default_season: int = Field(2024, env="DEFAULT_SEASON")
    session_cache_ttl_seconds: int = Field(60 * 60, env="SESSION_CACHE_TTL_SECONDS")  # FR-BE-10
    strategy_cache_ttl_seconds: int = Field(60 * 10, env="STRATEGY_CACHE_TTL_SECONDS")  # FR-BE-11

    # Redis cache
    redis_url: Optional[str] = Field(None, env="REDIS_URL")

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


@lru_cache()
def get_settings() -> AppSettings:
    """
    Cached settings instance.
    """
    return AppSettings()

