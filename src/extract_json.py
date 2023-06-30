from pathlib import Path
import json


def json_to_dict(json_path: str) -> dict:
    with open(json_path, "r") as f:
        match_dict = json.load(f)
    return match_dict


def get_matches(json_paths: list) -> tuple:
    match_ids = list()
    matches = list()
    json_paths = sorted(json_paths)
    for path in json_paths:
        match_data = json_to_dict(path)
        match_id = match_data["metadata"]["matchId"]
        match_ids.append(match_id)
        matches.append(match_data)
    return (match_ids, matches)


def is_player(player: dict, summoner_name: str) -> bool:
    return player["summonerName"] == summoner_name


# Returns the entire player stats
def get_player_stats(players: list, summoner_name: str) -> list:
    return list(filter(lambda x: is_player(x, summoner_name), players))


def curate_stats(player: dict, desired_stats: list, desired_challenges: list):
    all_stats = []
    for stat in desired_stats:
        all_stats.append(player[stat])
    for chal in desired_challenges:
        all_stats.append(player["challenges"][chal])
    return all_stats


def extract_match_data(summoner: str, stats: list, challenges: list) -> tuple:
    data_dir = Path.cwd() / "data"
    json_paths = [path for path in data_dir.iterdir() if path.suffix == '.json']

    matches = get_matches(json_paths)
    match_ids = matches[0]
    matches_data = matches[1]

    curated_data = list()
    for match in matches_data:
        players = match["info"]["participants"]
        player_stats = get_player_stats(players, summoner)[0]
        curated_player_stats = curate_stats(player_stats, stats, challenges)
        curated_data.append(curated_player_stats)
    return (match_ids, curated_data)
