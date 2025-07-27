import requests
from openf1_pydantic_models.f1_sessions import GetF1SessionsResponse
from constants.openf1_api_endpoints import SESSIONS_API_URL
from api_pydantic_models.races import RaceInfo


def get_races_by_year(year: int) -> list[RaceInfo]:
    parameters = {
        "year": year,
    }
    response = requests.get(SESSIONS_API_URL, params=parameters)
    response.raise_for_status()
    try:
        all_races = GetF1SessionsResponse(sessions=response.json())
        race_info = [RaceInfo(session_key=s.session_key, location=s.location, session_name=s.session_name) for s in all_races.sessions]
        return sorted(race_info, key=lambda x: x.location)
    except Exception as e:
        print(e)
