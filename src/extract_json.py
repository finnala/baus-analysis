import json


def json_to_dict(json_path: str) -> dict:
    with open(json_path, "r") as f:
        match_dict = json.load(f)
    return match_dict


def get_matches(json_paths: list) -> list:
    matches = list()
    for path in json_paths:
        match_data = json_to_dict(path)
        matches.append(match_data)
    return matches
