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
