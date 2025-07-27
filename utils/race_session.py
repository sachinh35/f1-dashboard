from openf1_pydantic_models.f1_sessions import GetF1SessionsResponse, F1SessionResult, GetF1SessionResultResponse
from constants.openf1_api_endpoints import SESSIONS_API_URL, SESSION_RESULTS_API_URL
from api_pydantic_models.races import RaceInfo
import httpx


async def get_races_by_year(year: int) -> list[RaceInfo]:
    parameters = {
        "year": year,
    }
    try:
        async with httpx.AsyncClient(timeout=10) as client:
            response = await client.get(SESSIONS_API_URL, params=parameters)

            all_races = GetF1SessionsResponse(sessions=response.json())
            race_info = [RaceInfo(session_key=s.session_key, location=s.location, session_name=s.session_name) for s in
                         all_races.sessions]
            return sorted(race_info, key=lambda x: x.location)
    except Exception as e:
        print(e)
        raise e


async def get_results_by_session_key(session_key: int) -> list[F1SessionResult]:
    parameters = {
        "session_key": session_key
    }
    try:
        async with httpx.AsyncClient(timeout=10) as client:
            response = await client.get(SESSION_RESULTS_API_URL, params=parameters)
            print("response: {}".format(response.json()))
            validated_response = GetF1SessionResultResponse(session_result=response.json())
            all_results = validated_response.session_result
            return sorted(all_results, key=lambda x: x.driver_number)
    except Exception as e:
        print(e)
        raise e
