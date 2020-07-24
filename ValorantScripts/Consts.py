API_KEY = "RGAPI-e4f2461d-843e-4e70-a85f-cf68b7719f42" # Changes daily

# Account calls for Riot Account API

ACCOUNT_URL = {
    'base' : "https://{region}.api.riotgames.com/riot/account/v{version}/accounts/{call_type}?api_key={api_key}",
    'by-puuid' : "by-puuid/{puuid}",
    'by-riot-id' : "by-riot-id/{inGameName}/{tagLine}",
}

ACCOUNT_API_VERSIONS = {
    'by-puuid' : "1",
    'by-riot-id' : "1"
}

ACCOUNT_REGIONS = ["AMERICAS", "ASIA", "EUROPE"]