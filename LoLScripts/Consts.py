API_KEY = open("API_KEY.txt", "r").read()  # Changes daily

# Account calls for Riot Account API

ACCOUNT_URL = {
    'base': "https://{region}.api.riotgames.com/riot/account/v{version}/accounts/{call_type}?api_key={api_key}",
    'by-puuid': "by-puuid/{puuid}",
    'by-riot-id': "by-riot-id/{inGameName}/{tagLine}",
}

ACCOUNT_API_VERSIONS = {
    'by-puuid': "1",
    'by-riot-id': "1"
}

ACCOUNT_REGIONS = ["AMERICAS", "ASIA", "EUROPE"]

LEAGUE_URL = {
    'base': "https://{region}.api.riotgames.com/lol/league/v{version}/{call_type}?api_key={api_key}",
    'by-league-entries': "entries/{queue}/{tier}/{division}",
    'by-summoner-id': "entries/by-summoner/{encryptedSummonerId}",
    'by-league': "{leagueType}/by-queue/{queue}",
    'top-leagues': "{tier}/by-queue/{queue}"
}

LEAGUE_QUEUE_TYPES = {
    "1": "RANKED_SOLO_5x5",
    "2": "RANKED_FLEX_SR"
}

LEAGUE_API_VERSIONS = {
    'version': "4",
}

LEAGUE_REGIONS = [
    "br1", "eun1", "euw1", "jp1", "kr", "la1", "la2", "na1", "oc1", "ru", "tr1"
]

LEAGUE_TOP_LEAGUES_TYPES = {
    "challenger": "challengerleagues",
    "grandmaster": "grandmasterleagues",
    "master": "masterleagues"
}

SUMMONER_URL = {
    'base': "https://{region}.api.riotgames.com/lol/summoner/v{version}/summoners/{call_type}/?api_key={api_key}",
    'by-summoner-name': "by-name/{summonerName}"
}

SUMMONER_API_VERSIONS = {
    'version': "4",
}

# https://na1.api.riotgames.com/lol/match/v4/matchlists/by-account/LFTpvbxYLsGS_jn22cW5s0jVRnyBWqYBn6toQfDyHdCvsvuSrowSwmFF?api_key=RGAPI-c0aeed68-f9b2-43f0-93a3-67192f41432e
MATCH_URL = {
    'base': "https://{region}.api.riotgames.com/lol/match/v{version}/{call_type}/?api_key={api_key}",
    'by-account': "matchlists/by-account/{encryptedAccountId}"
}


MATCH_API_VERSIONS = {
    'version': "4",
}

# Shared with Summoner and Match

LEAGUE_REGIONS = [
    "br1", "eun1", "euw1", "jp1", "kr", "la1", "la2", "na1", "oc1", "ru", "tr1"
]

COMMONS = {
    'queue': ["RANKED_SOLO_5x5", "RANKED_FLEX_SR", "RANKED_FLEX_TT"],
    'leagueType': ["masterleagues", "grandmasterleagues", "challengerleagues"],
    'tier': ["DIAMOND", "PLATINUM", "GOLD", "SILVER", "BRONZE", "IRON"],
    'division': ["I", "II", "III", "IV"],
}
