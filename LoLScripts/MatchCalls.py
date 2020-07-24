import requests
import Consts as Consts


class MatchAPI(object):
    def __init__(self, api_key):
        self.api_key = api_key

    def _get_match_history(self, encryptedAccountId, region):
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
        print(response.json())
