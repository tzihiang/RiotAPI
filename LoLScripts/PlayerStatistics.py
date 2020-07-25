import requests
import Champions

from AccountCalls import AccountAPI
from LeagueCalls import LeagueAPI
from MatchCalls import MatchAPI
from SummonerCalls import SummonerAPI
from Consts import API_KEY

ACCOUNT_DB = AccountAPI(API_KEY)
LEAGUE_DB = LeagueAPI(API_KEY)
MATCH_DB = MatchAPI(API_KEY)
SUMMONER_DB = SummonerAPI(API_KEY)

# Returns the user match history by inputting the summoner name and region

# Returns the most recent 100 matches of the user in a given region


def _get_match_history(summonerName, region):
    # First step is to fetch the user's account ID
    encryptedAccountId = SUMMONER_DB._get_accountID_from_summonerName(
        summonerName, region)

    # Next step is to fetch match history from MATCH_DB
    matchHistory = MATCH_DB._get_match_history(encryptedAccountId, region)

    return matchHistory


# def _get_role(match):
#     if (match['lane'] == "MID"):
#         return "MIDDLE"
#     elif (match['lane'] == "TOP"):
#         return "TOP"
#     elif (match['lane'] == "JUNGLE"):
#         return "JUNGLE"
#     elif (match['lane'] == "BOTTOM" and match['role'] == "DUO_CARRY"):
#         return "BOTTOM"
#     elif (match['lane'] == "BOTTOM" and match['role'] == "DUO_SUPPORT"):
#         return "SUPPORT"
#     else:
#         return "ROLE NOT FOUND"

# TODO: Get winrate per champion

def _get_champion_statistics(summonerName, region):
    matchHistory = _get_match_history(summonerName, region)['matches']
    champion_list = {}
    for match in matchHistory:
        c = Champions._get_champion_by_id(match['champion'])
        if c not in champion_list:
            champion_list[c] = 1
        else:
            champion_list[c] = int(champion_list.get(c)) + 1
    print(champion_list)


_get_champion_statistics("TheEichelTower88", "na1")
