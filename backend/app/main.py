from fastapi import FastAPI

from app.api.v1.routes import api_router as api_v1_router
from app.core.config import get_settings
from app.core.logging import setup_logging


def create_app() -> FastAPI:
    """
    Application factory.

    Wires versioned API routers and prepares the FastAPI instance.
    """
    setup_logging()
    settings = get_settings()

    app = FastAPI(
        title=settings.app_name,
        version="0.1.0",
        description="Backend service for the Formula 1 race strategy visualizer.",
        debug=settings.debug,
    )

    # Mount versioned API
    app.include_router(api_v1_router, prefix="/api")

    return app


app = create_app()


@app.get("/health", tags=["health"])
async def health_check() -> dict:
    """
    Simple health endpoint for uptime checks.
    """
    return {"status": "ok"}


