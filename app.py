import json
import os
from datetime import datetime

if not os.getenv('api_key'):
    exit('You must set an API key')
api_key = os.getenv('api_key')
import requests

response = requests.get(
    f"https://europe.api.riotgames.com/riot/account/v1/accounts/by-riot-id/Touplitoui/euw?api_key={api_key}")
response.raise_for_status()
data = response.json()
# print(data)
puuid = data['puuid']
summoner = data['gameName']
tagLine = data['tagLine']
basedir = os.path.dirname(__file__)
# print("basedir = {}".format(basedir))
response = requests.get(f"https://euw1.api.riotgames.com/lol/league/v4/entries/by-puuid/{puuid}?api_key={api_key}")
response.raise_for_status()
data = response.json()
all_profile = data[0]
with open(os.path.join(basedir, 'output', 'profile.json'), 'w') as f:
    f.write(json.dumps(all_profile, indent=4))

now_ts = int(datetime.now().timestamp())
start_period = now_ts - (3600 * 7)
print(now_ts)
print(start_period)
# exit()
response = requests.get(
    f"https://europe.api.riotgames.com/lol/match/v5/matches/by-puuid/{puuid}/ids?startTime={now_ts - (3600 * 24 * 3)}&endTime={now_ts}&type=ranked&start=0&count=20&api_key={api_key}")
response.raise_for_status()
data = response.json()
# print(data)
all_profile['history'] = {
    'games': [],
    'summary': {
        'wins': 0,
        'losses': 0,
    }
}
for match in data[:20]:
    # print(match)
    response = requests.get(
        f"https://europe.api.riotgames.com/lol/match/v5/matches/{match}?api_key=RGAPI-b531cd54-f50f-4a8c-8f1c-61cab1856836")
    response.raise_for_status()
    data = response.json()
    # print(data)
    # print(data['info'].keys())
    game_info = {}
    game_info['gameId'] = data['info']['gameId']
    game_info['gameStartTimestamp'] = data['info']['gameStartTimestamp']
    game_info['platformId'] = data['info']['platformId']
    game_info['gameType'] = data['info']['gameType']
    game_info['gameName'] = data['info']['gameName']
    game_info['gameMode'] = data['info']['gameMode']
    game_info['endOfGameResult'] = data['info']['endOfGameResult']
    game_info['gameDuration'] = data['info']['gameDuration']
    # game_info['participants'] = data ['info']['participants']
    myteam = None
    for p in data['info']['participants']:
        if puuid == p['puuid']:
            myteam = p['teamId']
    game_info['teams'] = []
    # print(data['info']['teams'][0].keys())
    # print(data['info']['teams'][0]['bans'])
    # print(data['info']['teams'][0]['feats'])
    # print(data['info']['teams'][0]['objectives'])
    # print(data['info']['teams'][0]['objectives'].keys())
    # exit()
    game_info['teams'].append({
        'teamId': data['info']['teams'][0]['teamId'],
        'win': data['info']['teams'][0]['win'],
        'myTeam': data['info']['teams'][0]['teamId'] == myteam,
    })
    game_info['teams'].append({
        'teamId': data['info']['teams'][1]['teamId'],
        'win': data['info']['teams'][1]['win'],
        'myTeam': data['info']['teams'][1]['teamId'] == myteam,
    })
    all_profile['history']['games'].append(game_info)


for match in all_profile['history']['games']:
    if (match['teams'][0]['win'] and match['teams'][0]['myTeam']) or (match['teams'][1]['win'] and match['teams'][1]['myTeam']):
        # print('win')
        all_profile['history']['summary']['wins'] += 1
    else:
        # print('loss')
        all_profile['history']['summary']['losses'] += 1

# https://europe.api.riotgames.com/lol/match/v5/matches/by-puuid/U24j2Os2QScUGZavBTv372sT8xakJ2qoaFRKwu9AG_4JZcZdS-kzz5idWBRK5N-ScHlg79Rxm8mrxA/ids?startTime=1751040301&endTime=1752045301&type=ranked&start=0&count=20&api_key=RGAPI-b531cd54-f50f-4a8c-8f1c-61cab1856836
print(all_profile)
with open(os.path.join(basedir, 'output', 'full_profile.json'), 'w') as f:
    f.write(json.dumps(all_profile, indent=4))