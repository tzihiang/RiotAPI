import requests
import RiotConsts as Consts

class RiotAPI(object): 

    def __init__(self, api_key, region):
        self.api_key = api_key
        self.region = region
    
    def _request(self, api_url, params={}):
        args = {'api_key': self.api_key}
        for key, value in params.items():
            if key not in args:
                args[key] = value
        response = requests.get(
            Consts.LOR_URL['base'].format(
                region=self.region,
                url=api_url
            ),
            params=args
        )
        print(response.url)
        return response.json()
    
    def get_all_leaderboard_info(self):
        api_url = Consts.LOR_URL['lor-leaderboards'].format(
            version=Consts.LOR_API_VERSIONS["LOR-RANKED"]
        )
        return self._request(api_url)


