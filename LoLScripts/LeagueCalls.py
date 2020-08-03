import requests
import Consts as Consts


class LeagueAPI(object):
    def __init__(self, api_key):
        self.api_key = api_key

    # This method retrieves a JSON based on queue, tier and division
    def _get_league_entries(self, region, queue, tier, division):
        response = requests.get(
            Consts.LEAGUE_URL['base'].format(
                region=region,
                version=Consts.LEAGUE_API_VERSIONS["version"],
                call_type=Consts.LEAGUE_URL['by-league-entries'].format(
                    queue=queue,
                    tier=tier,
                    division=division
                ),
                api_key=self.api_key
            )
        )
        return response.json()

    # Returns a list of summoners from the respective region, queue, tier and division
    def _get_summoners_from_division(self, region, queue, tier, division):
        r = self._get_league_entries(region, queue, tier, division)
        for items in r:
            print(items['summonerName'])

    # Returns a list of summonerIDs from the respective region and from challenger, GM or master
    def _retrieve_5X5_SOLO_info_json(self, region, tier):
        response = requests.get(
            Consts.LEAGUE_URL['base'].format(
                region=region,
                version=Consts.LEAGUE_API_VERSIONS['version'],
                call_type=Consts.LEAGUE_URL['top-leagues'].format(
                    tier=Consts.LEAGUE_TOP_LEAGUES_TYPES[tier],
                    queue=Consts.LEAGUE_QUEUE_TYPES["1"]
                ),
                api_key=self.api_key
            )
        )
        return response.json()

    # Retrieves all account IDs in 5v5 SOLO
    def _retrieve_5X5_SOLO_accountID(self, region, tier):
        summonerNames = []
        r = self._retrieve_5X5_SOLO_info_json(region, tier)
        for entries in r['entries']:
            summonerNames.append(entries['summonerName'])
        return summonerNames

    def _get_summoner_league_info(self, region, encryptedSummonerId):
        response = requests.get(
            Consts.LEAGUE_URL['base'].format(
                region=region,
                version=Consts.LEAGUE_API_VERSIONS["version"],
                call_type=Consts.LEAGUE_URL['by-summoner-id'].format(
                    encryptedSummonerId=encryptedSummonerId
                ),
                api_key=self.api_key
            )
        )
        return response.json()
