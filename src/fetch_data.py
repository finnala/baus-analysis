from dotenv import load_dotenv
import os
from pathlib import Path
from client import HTTPClient
from save_json_data import create_data_dir, match_data_to_json


load_dotenv()

API_KEY = os.environ.get("API_KEY")
client = HTTPClient(API_KEY)

player_puuid = client.get_puuid("Thebausffs")

match_ids = list()
intervals = [0, 100, 200, 300, 400]

for interval in intervals:
    match_list = client.get_match_ids(player_puuid, 100, interval)
    match_ids += match_list

create_data_dir()

for match in match_ids:
    data_dir = Path.cwd() / "data"
    json_paths = [path for path in data_dir.iterdir() if path.suffix == '.json']
    json_match_ids = [path.stem for path in json_paths]

    if match not in json_match_ids:
        print(f"Creating file for match {match}")
        match_data_to_json(client, match)
