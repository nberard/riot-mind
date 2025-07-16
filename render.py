import json
import os
from math import ceil

basedir = os.path.dirname(__file__)
print(basedir)
print(os.listdir(basedir))
with open(os.path.join(basedir, 'input_profile.json'), 'r') as fp:
    profile = json.loads(fp.read())
    with open(os.path.join(basedir, 'profile.template.html'), 'r') as pt:
        data: str = pt.read()
        res = data.format(rank=profile['tier'].lower(), name="Touplitoui", platform="EUW",
                          rankFull=profile['tier'] + " " + profile['rank'], gameNumber=4,
                          wins=profile['history']['summary']['wins'], losses=profile['history']['summary']['losses'],
                            winrate=ceil((profile['history']['summary']['wins'] / (profile['history']['summary']['wins'] + profile['history']['summary']['losses'])) * 100),
                          seasonWins=profile['wins'], seasonLosses=profile['losses'],
                            seasonWinrate=ceil((profile['wins'] / (profile['wins'] + profile['losses'])) * 100),
                          champion1='Zoe', nbKills=1, nbDeaths=1, nbAssists=1,kda=1, lp=profile['leaguePoints']
                          )
        with open(os.path.join(basedir, 'output/profile.html'), 'w') as rp:
            rp.write(res)


