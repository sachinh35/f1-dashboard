from pydantic import BaseModel
from typing import List
from enum import Enum


class SessionType(str, Enum):
    QUALIFYING = "Qualifying"
    RACE = "Race"


class GetAllSessionTypesResponse(BaseModel):
    session_types: List[SessionType]
