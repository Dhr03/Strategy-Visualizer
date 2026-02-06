from typing import List

from pydantic import BaseModel


class DriverSummary(BaseModel):
    code: str
    name: str
    team: str


class TeamSummary(BaseModel):
    name: str
    drivers: List[str]


class RaceMetadataResponse(BaseModel):
    """
    Response model for FR-BE-6.
    """

    race_name: str
    circuit: str
    total_laps: int
    drivers: List[DriverSummary]
    teams: List[TeamSummary]

