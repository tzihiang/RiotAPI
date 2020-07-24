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

# TODO


def _get_role_statistics(summonerName, region):
    matchHistory = _get_match_history(summonerName, region)['matches']
    print(matchHistory)


_get_role_statistics("TheEichelTower88", "na1")
