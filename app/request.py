import http.client
import json
from flask import request
import requests


def get_competitions():
    r=requests.get('https://api.football-data.org/v2/competitions/PL/matches?matchday=5',headers={ 'X-Auth-Token': '9b70f288df14443f994d4a1b89f3e4ac' } )


    return r.json
