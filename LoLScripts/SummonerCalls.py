import requests
import Consts as Consts


class SummonerAPI(object):
    def __init__(self, api_key):
        self.api_key = api_key

    def _get_summoner_info_from_summonerName(self, summonerName, region):
        response = requests.get(
            Consts.SUMMONER_URL['base'].format(
                region=region,
                version=Consts.SUMMONER_API_VERSIONS['version'],
                call_type=Consts.SUMMONER_URL['by-summoner-name'].format(
                    summonerName=summonerName
                ),
                api_key=self.api_key
            )
        )
        return response.json()

    def _get_accountID_from_summonerName(self, summonerName, region):
        return self._get_summoner_info_from_summonerName(summonerName, region)["accountId"]

    def _get_summonerId_from_summonerName(self, summonerName, region):
        return self._get_summoner_info_from_summonerName(summonerName, region)["id"]
