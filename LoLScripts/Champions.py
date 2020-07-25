import json

with open('json/en_US/champion.json', encoding="utf-8") as f:
    data = f.read()

champions = json.loads(data)

# r = requests.get(
#     "http://ddragon.leagueoflegends.com/cdn/10.14.1/data/en_US/champion.json").json()


def _get_champion_by_id(id):
    for k, v in champions['data'].items():
        if v['key'] == str(id):
            return v['id']
    return "CHAMPION NOT FOUND"
