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


def _get_summoner_champion_play_rate(summonerName, region):
    matchHistory = MATCH_DB._get_match_history(summonerName, region)['matches']
    champion_list = {}
    for matches in matchHistory:
        c = Champions._get_champion_by_id(matches['champion'])
        if c not in champion_list:
            champion_list[c] = 1
        else:
            champion_list[c] = int(champion_list.get(c)) + 1
    return(champion_list)

# Will calculate win rate over a certain number of games. Accepts an optional argument of the
# number of games calculated. 30 is the default.


def _get_summoner_win_rate(summonerName, region, max=30):
    # Returns a list of matches NOT matchIds
    matchHistory = MATCH_DB._get_match_history(summonerName, region)['matches']
    win = 0
    for matches in matchHistory[0:max]:
        id = matches["gameId"]
        if MATCH_DB._check_match_win(summonerName, region, id):
            win += 1
    return("Win rate = " + str(round(win/max * 100, 2)) + "% over " + str(max) + " games")


def _get_summoner_champion_win_rate(summonerName, region, max=30):
    matchHistory = MATCH_DB._get_match_history(summonerName, region)['matches']
    win_rates = {}
    for matches in matchHistory[0:max]:
        c = Champions._get_champion_by_id(matches['champion'])
        # First is to check if champion exists. The win rate will be stored in a dictionary
        # of lists. Eg. {Yorick: [0,0]} = [win, total]
        if c not in win_rates:
            win_rates[c] = [0, 0]
        # List will exist. Now to add accoding to win rate
        if MATCH_DB._check_match_win(summonerName, region, matches["gameId"]):
            win_rates[c][0] += 1
        win_rates[c][1] += 1
    for champion in win_rates:
        win_rates[champion] = str(
            round(win_rates[champion][0]/win_rates[champion][1] * 100, 2)) + " % over " + str(win_rates[champion][1]) + " games"
    return win_rates


print(_get_summoner_champion_win_rate("TSM", "na1", 10))
