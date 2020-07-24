import sys

from Consts import API_KEY as API_KEY
from Consts import ACCOUNT_REGIONS as region
from Consts import COMMONS as c
from Consts import LEAGUE_REGIONS as lr
from AccountCalls import AccountAPI
from LeagueCalls import LeagueAPI
from MatchCalls import MatchAPI
from SummonerCalls import SummonerAPI


def main():
    # api = AccountAPI(API_KEY, region[0])
    # puuid = api._get_puuid(sys.argv[1], sys.argv[2])
    # print(puuid)

    # api = LeagueAPI(API_KEY)
    # api._get_summoners_from_division(lr[7], c['queue'][0],
    #                                  c['tier'][5], c['division'][3])

    # api = SummonerAPI(API_KEY)
    # api._get_accountID_from_summonerName("TheEichelTower88", "na1")

    api = MatchAPI(API_KEY)
    api._get_match_history(
        "LFTpvbxYLsGS_jn22cW5s0jVRnyBWqYBn6toQfDyHdCvsvuSrowSwmFF", "na1")


if __name__ == "__main__":
    main()
