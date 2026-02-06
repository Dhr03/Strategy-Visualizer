from typing import Any

import fastf1

from app.core.config import get_settings


def load_session(season: int, round: int, session_type: str = "R") -> Any:
    """
    FR-BE-1: Session Loader

    Uses FastF1 to load a session. Caching will be enabled globally by FastF1.
    """
    settings = get_settings()

    # Enable FastF1 on-disk cache (location can be customized later)
    fastf1.Cache.enable_cache()

    # NOTE: Error handling and mapping to HTTP errors are handled at the service/router layer.
    session = fastf1.get_session(season, round, session_type)
    session.load()
    return session

