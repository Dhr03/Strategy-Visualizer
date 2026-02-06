from __future__ import annotations

from enum import Enum
from typing import List, Optional

from pydantic import BaseModel, Field


class TireCompound(str, Enum):
    SOFT = "SOFT"
    MEDIUM = "MEDIUM"
    HARD = "HARD"
    INTERMEDIATE = "INTERMEDIATE"
    WET = "WET"


class Stint(BaseModel):
    """
    Mirrors the frontend Strategy DTO definition.
    """

    stint_number: int = Field(..., alias="stintNumber")
    compound: TireCompound
    start_lap: int = Field(..., alias="startLap")
    end_lap: int = Field(..., alias="endLap")
    length: int

    class Config:
        allow_population_by_field_name = True


class Strategy(BaseModel):
    driver: str
    team: str
    total_laps: int = Field(..., alias="totalLaps")
    stints: List[Stint]
    pit_stops: List[int] = Field(..., alias="pitStops")

    class Config:
        allow_population_by_field_name = True


class DriverStrategyResponse(BaseModel):
    """
    Response model for FR-BE-7.
    """

    driver: str
    total_laps: int
    stints: List[Stint]
    pit_stops: List[int] = Field(..., alias="pitStops")

    class Config:
        allow_population_by_field_name = True


class TeamStrategyResponse(BaseModel):
    """
    Response model for FR-BE-8.
    """

    team: str
    drivers: List[DriverStrategyResponse]


class StrategyCompareRequest(BaseModel):
    """
    Request body for FR-BE-9.
    """

    drivers: List[str]
    season: Optional[int] = None
    round: Optional[int] = None


class StrategyCompareResponse(BaseModel):
    """
    Response body for FR-BE-9.
    """

    strategies: List[Strategy]

