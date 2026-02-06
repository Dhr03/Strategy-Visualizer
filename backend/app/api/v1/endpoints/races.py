from fastapi import APIRouter, HTTPException

from app.schemas.race import RaceMetadataResponse

router = APIRouter()


@router.get("/{season}/{round}", response_model=RaceMetadataResponse)
async def get_race_metadata(season: int, round: int) -> RaceMetadataResponse:
    """
    FR-BE-6: Race Metadata Endpoint

    NOTE: This is a placeholder implementation. The actual logic will:
    - Use FastF1 to load the specified session
    - Extract race name, circuit, total laps, drivers and teams.
    """
    # TODO: Implement integration with FastF1 session loader service.
    raise HTTPException(status_code=501, detail="Race metadata endpoint not implemented yet.")

