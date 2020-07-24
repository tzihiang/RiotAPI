from LoR_RiotAPI import RiotAPI
from RiotConsts import API_TOKEN as API_KEY
from RiotConsts import LOR_REGIONS as region


def main():
    api = RiotAPI(API_KEY, region["1"])
    ranked_info = api.get_all_leaderboard_info()
    playerArray = ranked_info["players"]
    print(playerArray)
    
if __name__ == "__main__":
    main()