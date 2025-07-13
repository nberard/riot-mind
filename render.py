import json
import os

basedir = os.path.dirname(__file__)
print(basedir)
print(os.listdir(basedir))
with open(os.path.join(basedir, 'input_profile.json'), 'r') as fp:
    profile = json.loads(fp.read())
    with open(os.path.join(basedir, 'profile.template.html'), 'r') as pt:
        data: str = pt.read()
        res = data.format(rank=profile['tier'].lower(), name="Touplitoui", platform="EUW",
                          rankFull=profile['tier'] + " " + profile['rank'], gameNumber=4,
                          champion1='Zoe', nbKills=1, nbDeaths=1, nbAssists=1,kda=1, lp=profile['leaguePoints']
                          )
        with open(os.path.join(basedir, 'output/res.html'), 'w') as rp:
            rp.write(res)


