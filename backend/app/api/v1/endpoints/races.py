from fastapi import APIRouter, HTTPException

from app.schemas.race import RaceMetadataResponse
from app.core.logging import get_logger
from app.services.session_service import load_session

router = APIRouter()
logger = get_logger(__name__)

@router.get("/{season}/{round}", response_model=RaceMetadataResponse)
async def get_race_metadata(season: int, round: int) -> RaceMetadataResponse:
    """
    FR-BE-6: Race Metadata Endpoint

    NOTE: This is a placeholder implementation. The actual logic will:
    - Use FastF1 to load the specified session
    - Extract race name, circuit, total laps, drivers and teams.
    """
    # TODO: Implement integration with FastF1 session loader service.
    try:
        session = load_session(season=season, round=round)
    except Exception as e:
        logger.error("Error encountered.")
        logger.error(str(e))
    raise HTTPException(status_code=500, detail="Something went wrong while fetching race metadata.\nPlease check logs.")

