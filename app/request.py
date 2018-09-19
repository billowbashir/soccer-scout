
import urllib.request,json
from flask import request

from .models import EplStandings

apikey='565ec012251f932ea4000001fa542ae9d994470e73fdb314a8a56d76'
baseurl='http://api.football-api.com/2.0/standings/1204?Authorization={}'
# 'http://api.football-api.com/2.0/matches/{}?Authorization={}''

def get_competitions():
    # r=requests.get('https://api.football-data.org/v2/competitions/PL/matches?matchday=5',headers={ 'X-Auth-Token': '9b70f288df14443f994d4a1b89f3e4ac' } )
    get_standings_url = baseurl.format(apikey)
    with urllib.request.urlopen(get_standings_url) as url:
        get_standings_data = url.read()
        get_standings_response = json.loads(get_standings_data)

        standings_results = None

        if get_standings_response:
            standings_results_list = get_standings_response
            standing_results = process_results(standings_results_list)


    return standing_results

def process_results(table_list):

    standing_results = []
    for table_item in table_list:
        position= table_item.get('position')
        team_name = table_item.get('team_name')
        matches=table_item.get('round')
        wins=table_item.get('overall_w')
        draws=table_item.get('overall_d')
        losses=table_item.get('overall_l')
        goaldifference=table_item.get('gd')
        points=table_item.get('points')
        standing_object = EplStandings(position,team_name,matches,wins,draws,losses,goaldifference,points)
        standing_results.append(standing_object)
    return standing_results
