from pydantic import BaseModel
from datetime import datetime
from typing import List


class F1Session(BaseModel):
    circuit_key: int
    circuit_short_name: str
    country_code: str
    country_key: int
    country_name: str
    date_end: datetime
    date_start: datetime
    gmt_offset: str
    location: str
    meeting_key: int
    session_key: int
    session_name: str
    session_type: str
    year: int


class GetF1SessionsResponse(BaseModel):
    sessions: List[F1Session]
