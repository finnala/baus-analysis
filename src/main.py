from dotenv import load_dotenv
import os
from client import HTTPClient


load_dotenv()

API_KEY = os.environ.get("API_KEY")
client = HTTPClient(API_KEY)

player_puuid = client.get_puuid("Thebausffs")

match_ids = list()
intervals = [0, 100, 200, 300, 400]

for interval in intervals:
    match_list = client.get_match_ids(player_puuid, 100, interval)
    match_ids += match_list
