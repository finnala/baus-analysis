from pathlib import Path
import json


def create_data_dir() -> None:
    dir_name = "data"
    dir = Path(dir_name)
    if not dir.exists():
        dir.mkdir()


def match_data_to_json(client: object, match_id: str) -> None:
    match_data = client.get_match_data(match_id)
    with open(f"data/{match_id}.json", "w", encoding="utf-8") as outfile:
        json.dump(match_data, outfile, indent=2)
