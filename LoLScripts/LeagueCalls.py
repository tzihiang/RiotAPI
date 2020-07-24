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

    # Returns a list of summoner from the respective region, queue, tier and division
    def _get_summoners_from_division(self, region, queue, tier, division):
        r = self._get_league_entries(region, queue, tier, division)
        for items in r:
            print(items['summonerName'])

    # def _find_summoner(self, summonerName):
