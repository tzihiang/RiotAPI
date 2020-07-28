import requests
import Consts as Consts

from Consts import API_KEY
from SummonerCalls import SummonerAPI


SUMMONER_DB = SummonerAPI(API_KEY)


class MatchAPI(object):
    def __init__(self, api_key):
        self.api_key = api_key

    def _get_match_history_by_encryptedAccountId(self, encryptedAccountId, region):
        response = requests.get(
            Consts.MATCH_URL['base'].format(
                region=region,
                version=Consts.MATCH_API_VERSIONS['version'],
                call_type=Consts.MATCH_URL['by-account'].format(
                    encryptedAccountId=encryptedAccountId
                ),
                api_key=self.api_key
            )
        )
        return response.json()

    # Returns all the matches from a particular summoner and region
    def _get_match_history(self, summonerName, region):
        # First step is to fetch the user's account ID
        encryptedAccountId = SUMMONER_DB._get_accountID_from_summonerName(
            summonerName, region)

        # Next step is to fetch match history from MATCH_DB
        matchHistory = self._get_match_history_by_encryptedAccountId(
            encryptedAccountId, region)

        return matchHistory

    def _get_match_ids_from_summoner(self, summonerName, region):
        matches = []
        for match in self._get_match_history(summonerName, region)['matches']:
            matches.append(match['gameId'])
        return matches
