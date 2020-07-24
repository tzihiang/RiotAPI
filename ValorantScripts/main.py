import sys

from Consts import API_KEY as API_KEY
from Consts import ACCOUNT_REGIONS as region
from AccountCalls import AccountAPI

def main():
    api = AccountAPI(API_KEY, region[0])
    puuid = api._get_puuid(sys.argv[1], sys.argv[2])
    print(puuid)
    
if __name__ == "__main__":
    main()