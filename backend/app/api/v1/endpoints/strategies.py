from fastapi import APIRouter, HTTPException, Query

from app.schemas.strategy import DriverStrategyResponse, StrategyCompareRequest, StrategyCompareResponse, TeamStrategyResponse

router = APIRouter()


@router.get("/driver", response_model=DriverStrategyResponse)
async def get_driver_strategy(
    season: int = Query(..., ge=1950),
    round: int = Query(..., ge=1),
    driver_code: str = Query(..., min_length=2, max_length=3),
) -> DriverStrategyResponse:
    """
    FR-BE-7: Driver Strategy Endpoint

    Placeholder implementation that will eventually call the strategy service.
    """
    # TODO: Integrate with strategy_service.get_driver_strategy
    raise HTTPException(status_code=501, detail="Driver strategy endpoint not implemented yet.")


@router.get("/team", response_model=TeamStrategyResponse)
async def get_team_strategy(
    season: int = Query(..., ge=1950),
    round: int = Query(..., ge=1),
    team_name: str = Query(..., min_length=2),
) -> TeamStrategyResponse:
    """
    FR-BE-8: Team Strategy Endpoint

    Placeholder implementation that will eventually call the strategy service.
    """
    # TODO: Integrate with strategy_service.get_team_strategy
    raise HTTPException(status_code=501, detail="Team strategy endpoint not implemented yet.")


@router.post("/compare", response_model=StrategyCompareResponse)
async def compare_strategies(payload: StrategyCompareRequest) -> StrategyCompareResponse:
    """
    FR-BE-9: Multi-Driver Compare Endpoint

    Placeholder implementation that will eventually call the strategy service.
    """
    # TODO: Integrate with strategy_service.compare_driver_strategies
    raise HTTPException(status_code=501, detail="Strategy compare endpoint not implemented yet.")

