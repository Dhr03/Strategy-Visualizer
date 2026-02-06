from typing import Dict, List

import pandas as pd

from app.schemas.strategy import DriverStrategyResponse, Strategy, Stint, TireCompound
from app.utils.tires import normalize_compound


def _extract_lap_data(session) -> pd.DataFrame:
    """
    FR-BE-2: Lap Data Extraction

    Placeholder structure that will use FastF1 laps dataframe.
    """
    # TODO: Implement real extraction from FastF1 session.laps
    raise NotImplementedError("Lap data extraction not implemented yet.")


def _compute_driver_stints(laps_df: pd.DataFrame) -> Dict[str, DriverStrategyResponse]:
    """
    FR-BE-3/4/5: Core strategy computation pipeline.

    This is currently a stub to be implemented later.
    """
    # TODO: Implement algorithm:
    # 1. Sort laps by lap number per driver
    # 2. Detect stint boundaries based on compound change or pit stop
    # 3. Aggregate to Strategy/DriverStrategyResponse objects
    raise NotImplementedError("Strategy computation not implemented yet.")


def get_driver_strategy(season: int, round: int, driver_code: str) -> DriverStrategyResponse:
    """
    Public service used by the driver strategy endpoint.
    """
    # TODO: Wire to session_service and caching layer.
    raise NotImplementedError("Driver strategy service not implemented yet.")


def get_team_strategy(season: int, round: int, team_name: str) -> List[DriverStrategyResponse]:
    """
    Public service used by the team strategy endpoint.
    """
    raise NotImplementedError("Team strategy service not implemented yet.")


def compare_driver_strategies(season: int, round: int, drivers: List[str]) -> List[Strategy]:
    """
    Public service used by the compare endpoint.
    """
    raise NotImplementedError("Strategy compare service not implemented yet.")

