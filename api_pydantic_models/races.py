from pydantic import BaseModel
from typing import List


class GetAvailableYearsResponse(BaseModel):
    years_list: List[int]


class GetRacesForYearsResponse(BaseModel):
    all_races: List[str]
