# RiotAPI
### My own personal scripts to call from riots API available at: https://developer.riotgames.com/apis

### These scripts are for personal use and are not developed into a library yet. 

### The libraries here are specific for League of Legends only. Please refer to LoLScripts and use the libraries there. LoR and Valorant scripts are currently not done as the API is currently not available.

## Prerequisites
### 1. Have python3 installed, available [here](https://www.python.org/downloads/ "Install python 3 here!")
### 2. Retrieve your own API Key from Riot. In order to prevent the misuse of individual API Keys, I have made a way to easily integrate your own API key so you can use the library straightaway. Create an empty API_KEY.txt file and paste your API key inside and you are done! It should be in the LoLScripts folder, which is the same level as main.py.
### 3. This library is currently up to date (as of 3rd Aug 2020) and works with DDragon version 10.14.1. Please place the Assets and Json folders from your DDragon in LoLScripts, which is the same level as main.py.


## Navigating the library
### main.py is the main driver behind all the information you would want to retrieve. It directly imports all the calls from the library.
### Consts.py consists of constants that are rarely changed and should not be touched unless Riot chooses to change the naming convention of its request URLs.
### Call scripts (with the suffix -Calls.py) such as MatchCalls.py are calls that are specifically made towards the API categorised by riot [here](https://developer.riotgames.com/apis). This is done to acheive order between the call types so that troubleshooting would be done easier. 
### PlayerStatistics.py and GlobalStatistics.py are player and global specific respectively, which will be covered later on.
### Champions.py requires you to import DDragon, so please do so correctly! In order to support future releases of DDragon, I chose not to directly call from their json version of it on URL since the URL is always changing. Instead, updating DDragon might be easier and more up-to-date. Please let me know if you have any suggestions to streamline this process to prevent the cumbersome process of updating everytime a new patch is out!

## Functions in PlayerStatistics:
### PlayerStatistics needs at least the Summoner's name and respective region minimally in order to work. All the fetching of summoner and account IDs have already been handled by the calls. For regions, it is only limited to the regions currently available on Riot's website. Namely: ```"br1", "eun1", "euw1", "jp1", "kr", "la1", "la2", "na1", "oc1", "ru", "tr1"```

1. ```_get_summoner_champion_play_rate(summonerName, region, max)``` 

    Returns the play rate of specific champions the summoner in the given region, in a form of a dictionary. Max is an optional parameter and refers to the amount of games to calculate. If not supplied, will run with the default of the latest 30 matches. 

    Example output: ```{'Lux': 1, 'Caitlyn': 10, 'Jinx': 15, 'Hecarim': 1, 'LeeSin': 1, 'Aphelios': 1, 'Varus': 1}```
2. ```_get_summoner_win_rate(summonerName, region, max)```
    
    Returns the win rate of the summoner in the given region. Max is an optional parameter and refers to the amount of games to calculate. If not supplied, will run with the default of the latest 30 matches. 

    Example output: ```Win rate = 50.0% over 30 games```
    
    Note: This is a rather expensive process to handle, since this library is made to handle real-time data fetched from Riot's servers. If deployed, it is highly recommended to cache high traffic searches to lower the number of fetches, as well as for a faster lookup.
3. ```_get_summoner_champion_win_rate(summonerName, region, max)```

    Returns the win rate of champions of the summoner in the given region, in the form of a dictionary. Max is an optional parameter and refers to the amount of games to calculate. If not supplied, will run with the default of the latest 30 matches. 

    Example output: ```{'Lux': '0.0 % over 1 game(s)', 'Caitlyn': '50.0 % over 10 game(s)', 'Jinx': '60.0 % over 15 game(s)', 'Hecarim': '0.0 % over 1 game(s)', 'LeeSin': '100.0 % over 1 game(s)', 'Aphelios': '0.0 % over 1 game(s)', 'Varus': '0.0 % over 1 game(s)'}```

    Note: Just like getting summoner win rate, it is also a expensive process to handle, since this library is made to handle real-time data fetched from Riot's servers. If deployed, it is highly recommended to cache high traffic searches to lower the number of fetches, as well as for a faster lookup.
4. ```_get_summoner_ranked_stats(summonerName, region)```

    Returns and tier and rank of the summoner in the given region.

    Example output: ```GOLD IV```

## Functions of GlobalStatistics:
### Global Statistics is still a work in progress, as fetching all the data is a very expensive process (at least the way I see it) and I cannot get it running in real time fetches. If you have any idea, do feel free to contribute or give suggestions as you see fit!
