from fastapi import APIRouter

from app.api.v1.endpoints import races, strategies


api_router = APIRouter()

# Race metadata
api_router.include_router(races.router, prefix="/races", tags=["races"])

# Strategy-related endpoints
api_router.include_router(strategies.router, prefix="/strategies", tags=["strategies"])

