import json
import os

if not os.getenv('api_key'):
    exit('You must set an API key')
api_key = os.getenv('api_key')
import requests
response = requests.get(f"https://europe.api.riotgames.com/riot/account/v1/accounts/by-riot-id/Touplitoui/euw?api_key=RGAPI-b531cd54-f50f-4a8c-8f1c-61cab1856836")
response.raise_for_status()
data = response.json()
# print(data)
puuid = data['puuid']
summoner = data['gameName']
tagLine = data['tagLine']

response = requests.get(f"https://euw1.api.riotgames.com/lol/league/v4/entries/by-puuid/{puuid}?api_key={api_key}")
response.raise_for_status()
data = response.json()
all_profile = data[0]
with open('profile.json', 'w') as f:
    f.write(json.dumps(all_profile, indent=4))

response = requests.get(f"https://europe.api.riotgames.com/lol/match/v5/matches/by-puuid/U24j2Os2QScUGZavBTv372sT8xakJ2qoaFRKwu9AG_4JZcZdS-kzz5idWBRK5N-ScHlg79Rxm8mrxA/ids?startTime=1751040301&endTime=1752045301&type=ranked&start=0&count=20&api_key=RGAPI-b531cd54-f50f-4a8c-8f1c-61cab1856836")
response.raise_for_status()
data = response.json()
print(data)
all_profile['history'] = []
for match in data[:5]:
    print(match)
    response = requests.get(
        f"https://europe.api.riotgames.com/lol/match/v5/matches/{match}?api_key=RGAPI-b531cd54-f50f-4a8c-8f1c-61cab1856836")
    response.raise_for_status()
    data = response.json()
    print(data)
    print(data['info'].keys())
    game_info = {}
    game_info['gameId'] = data['info']['gameId']
    game_info['gameStartTimestamp'] = data['info']['gameStartTimestamp']
    game_info['platformId'] = data['info']['platformId']
    game_info['gameType'] = data['info']['gameType']
    game_info['gameName'] = data['info']['gameName']
    game_info['gameMode'] = data['info']['gameMode']
    game_info['endOfGameResult'] = data['info']['endOfGameResult']
    game_info['gameDuration'] = data['info']['gameDuration']
    game_info['teams'] = []
    game_info['teams'].append({
        'teamId': data['info']['teams'][0]['teamId'],
        'win': data['info']['teams'][0]['win'],
    })
    game_info['teams'].append({
        'teamId': data['info']['teams'][1]['teamId'],
        'win': data['info']['teams'][1]['win'],
    })
    print(game_info)
    all_profile['history'].append(game_info)

with open('full_profile.json', 'w') as f:
    f.write(json.dumps(all_profile, indent=4))

# for match in all_profile['history']:


# https://europe.api.riotgames.com/lol/match/v5/matches/by-puuid/U24j2Os2QScUGZavBTv372sT8xakJ2qoaFRKwu9AG_4JZcZdS-kzz5idWBRK5N-ScHlg79Rxm8mrxA/ids?startTime=1751040301&endTime=1752045301&type=ranked&start=0&count=20&api_key=RGAPI-b531cd54-f50f-4a8c-8f1c-61cab1856836