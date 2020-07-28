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

matchIDs = []
region = "na1"

# 1. Retrieve list of summoner Names
summonerNames = LEAGUE_DB._retrieve_5X5_SOLO_accountID(region, "challenger")

# 2. Append those match histories into a global array matchIDs
for summoner in summonerNames:
    try:
        print(MATCH_DB._get_match_ids_from_summoner(summoner, region))
    except:
        print(type(summoner))
