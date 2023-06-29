import time
import requests


class HTTPClient:
    def __init__(self, api_key) -> None:
        self.api_key = api_key
        self.session = requests.session()
        self.session.headers.update({"X-Riot-Token": self.api_key})

    # TODO: Either make decorator function, or redo. Very rudimentary throttling
    # method to overcome rate limiting, but gets the job done for now.
    def throttle(self) -> None:
        time.sleep(2)

    def get_puuid(self, summoner_name: str) -> str:
        url = "https://euw1.api.riotgames.com/lol/summoner/v4/summoners/by-name"
        response = self.session.get(f"{url}/{summoner_name}")
        self.throttle()
        response.raise_for_status()

        puuid = response.json()["puuid"]
        return puuid

    def get_match_ids(self, puuid: str, count: int, start=0) -> list:
        url = "https://europe.api.riotgames.com/lol/match/v5/matches/by-puuid"
        payload = {
            "queue": 420,
            "type": "ranked",
            "start": start,
            "count": count,
        }
        response = self.session.get(f"{url}/{puuid}/ids", params=payload)
        self.throttle()
        response.raise_for_status()

        return response.json()

    def get_match_data(self, match_id: str) -> dict:
        url = "https://europe.api.riotgames.com/lol/match/v5/matches"

        response = self.session.get(f"{url}/{match_id}")
        self.throttle()
        response.raise_for_status()
        return response.json()
