import json
import os


with open('full_profile.json', 'r') as fp:
    profile = json.loads(fp.read())
    with open('profile.template.html', 'r') as pt:
        data: str = pt.read()
        res = data.format(rank=profile['tier'].lower(), name="Touplitoui", platform="EUW",
                          rankFull=profile['tier'] + " " + profile['rank'], gameNumber=4,
                          champion1='Zoe', nbKills=1, nbDeaths=1, nbAssists=1,kda=1, lp=profile['leaguePoints']
                          )
        with open('res.html', 'w') as rp:
            rp.write(res)


