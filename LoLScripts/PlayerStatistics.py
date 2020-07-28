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

# TODO: Get winrate per champion


def _get_champion_statistics_of_summoner(summonerName, region):
    matchHistory = MATCH_DB._get_match_history(summonerName, region)['matches']
    champion_list = {}
    for match in matchHistory:
        c = Champions._get_champion_by_id(match['champion'])
        if c not in champion_list:
            champion_list[c] = 1
        else:
            champion_list[c] = int(champion_list.get(c)) + 1
    return(champion_list)

# Will calculate win rate over a certain number of games. Accepts an optional argument of the
# number of games calculated. 30 is the default.


def _calculate_win_rate(summonerName, region, max=30):
    # Returns a list of matches NOT matchIds
    matchHistory = MATCH_DB._get_match_history(summonerName, region)['matches']
    win = 0
    for matches in matchHistory[0:max]:
        id = matches["gameId"]
        # print(MATCH_DB._check_match_win(summonerName, region, id))
        if MATCH_DB._check_match_win(summonerName, region, id):
            win += 1
    return("Win rate = " + str(round(win/max * 100)) + "% over " + str(max) + " games")


# print(_calculate_win_rate("TSM", "na1", 10))
# _get_champion_statistics_of_summoner("TheEichelTower88", "na1")
