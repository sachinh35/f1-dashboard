from pydantic import BaseModel
from datetime import datetime
from typing import List, Union


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


class F1SessionResult(BaseModel):
    dnf: bool
    dns: bool
    dsq: bool
    driver_number: int
    duration: List[Union[float, None]]
    gap_to_leader: List[Union[float, None]]
    number_of_laps: int
    meeting_key: Union[int, str]
    position: int
    session_key: int


class GetF1SessionsResponse(BaseModel):
    sessions: List[F1Session]


class GetF1SessionResultResponse(BaseModel):
    session_result: List[F1SessionResult]
