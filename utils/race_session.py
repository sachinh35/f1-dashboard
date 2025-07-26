import requests
from openf1_pydantic_models.f1_sessions import GetF1SessionsResponse
from constants.openf1_api_endpoints import SESSIONS_API_URL


def get_races_by_year(year: int) -> list[str]:
    parameters = {
        "year": year,
        "session_type": "Race"
    }
    response = requests.get(SESSIONS_API_URL, params=parameters)
    response.raise_for_status()
    try:
        all_races = GetF1SessionsResponse(sessions=response.json())
        circuits = [s.location for s in all_races.sessions]
        return circuits
    except Exception as e:
        print(e)
