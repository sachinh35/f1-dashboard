from pydantic import BaseModel
from typing import List
from enum import Enum
from openf1_pydantic_models.f1_sessions import F1SessionResult


class SessionType(str, Enum):
    QUALIFYING = "Qualifying"
    RACE = "Race"


class GetAllSessionTypesResponse(BaseModel):
    session_types: List[SessionType]


class GetSessionResultsResponse(BaseModel):
    results: List[F1SessionResult]
