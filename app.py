import os
#
# from flask import Flask, render_template
#
# app = Flask(__name__)
# @app.route("/")
# def index():
#     if not os.getenv('api_key'):
#         exit('You must set an API key')
#     api_key = os.getenv('api_key')
#     import requests
#     response = requests.get(f"https://europe.api.riotgames.com/riot/account/v1/accounts/by-riot-id/Touplitoui/euw?api_key={api_key}")
#     response.raise_for_status()
#     data = response.json()
#     puuid = data['puuid']
#     summoner = data['gameName']
#     tagLine = data['tagLine']
#
#     #print(data)
#     response = requests.get(f"https://euw1.api.riotgames.com/lol/league/v4/entries/by-puuid/{puuid}?api_key={api_key}")
#     response.raise_for_status()
#     data = response.json()
#     print(data)
#
#
#
# if __name__ == '__main__':
#     app.run(debug=True, host='127.0.0.1', port=5000)

from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello World!"

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')
