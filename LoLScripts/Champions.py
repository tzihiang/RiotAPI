import requests

r = requests.get(
    "http://ddragon.leagueoflegends.com/cdn/10.14.1/data/en_US/champion.json").json()


def _get_champion_by_id(id):
    cleaned_json = r['data']
    for k, v in cleaned_json.items():
        if (v['key'] == str(id)):
            return k
    return "Champion not found"
