API_TOKEN = "RGAPI-4c05b643-e3d0-45f7-8fd0-1bc998431fca" # Changes daily

#############
# LOR CALLS #
#############

LOR_URL = {
    'base': "https://{region}.api.riotgames.com/{url}",
    'lor-leaderboards': "lor/ranked/v{version}/leaderboards"
}

LOR_API_VERSIONS = {
    'LOR-RANKED' : '1'
}

LOR_REGIONS = {
    '1': 'asia',
    '2' : 'americas',
    '3' : 'europe',
    '4' : 'SEA'
}