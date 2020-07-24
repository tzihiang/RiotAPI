import requests
import Consts as Consts


class AccountAPI(object):
    def __init__(self, api_key):
        self.api_key = api_key

    # Returns the user's puuid when we user enters inGameName and tagLine
    def _get_puuid(self, inGameName, tagLine, region):
        response = requests.get(
            Consts.ACCOUNT_URL['base'].format(
                region=region,
                version=Consts.ACCOUNT_API_VERSIONS['by-riot-id'],
                call_type=Consts.ACCOUNT_URL['by-riot-id'].format(
                    inGameName=inGameName,
                    tagLine=tagLine
                ),
                api_key=self.api_key
            )
        )
        return response.json()["puuid"]
