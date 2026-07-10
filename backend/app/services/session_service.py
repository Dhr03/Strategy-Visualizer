from typing import Any
import fastf1

from app.core.logging import get_logger

logger = get_logger(__name__)


def load_session(season: int, round: int, session_type: str = "R") -> fastf1.core.Session:
    """
    FR-BE-1: Session Loader

    Uses FastF1 to load a session. Caching will be enabled globally by FastF1.
    """
    logger.info(f"Loading race session for season {season} round {round}...")

    # Enable FastF1 on-disk cache (location can be customized later)
    # fastf1 already has cache enable by default and cache hits are not counted towards rate limits.
    # fastf1.Cache.enable_cache()

    # NOTE: Error handling and mapping to HTTP errors are handled at the service/router layer.
    session = fastf1.get_session(season, round, session_type)
    session.load(weather=False)
    return session

