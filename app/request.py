
import urllib.request,json
from flask import request

from .models import EplStandings,FixtureList,MatchDetails


apikey='565ec012251f932ea4000001fa542ae9d994470e73fdb314a8a56d76'
baseurl='http://api.football-api.com/2.0/standings/1204?Authorization={}'

fixture_baseurl='http://api.football-api.com/2.0/matches?comp_id=1204&from_date=15.9.2018&to_date=24.9.2018&Authorization={}'
details_url='http://api.football-api.com/2.0/commentaries/{}?Authorization={}'
# request for standings
def get_competitions():
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

    # request for fixture
def get_fixtures():
    get_fixture_url = fixture_baseurl.format(apikey)
    with urllib.request.urlopen(get_fixture_url) as url:
        get_fixture_data = url.read()
        get_fixture_response = json.loads(get_fixture_data)

        fixtures_results = None

        if get_fixture_response:
            fixtures_results_list = get_fixture_response
            fixture_results = process_fixture_results(fixtures_results_list)


    return fixture_results


def process_fixture_results(fixture_list):
    fixture_results = []
    for fixture_item in fixture_list:
        id=fixture_item.get('id')
        venue= fixture_item.get('venue')
        status = fixture_item.get('status')
        localteam_name=fixture_item.get('localteam_name')
        localteam_score=fixture_item.get('localteam_score')
        visitorteam_name=fixture_item.get('visitorteam_name')
        visitorteam_score=fixture_item.get('visitorteam_score')
        time=fixture_item.get('time')

        formatted_date = fixture_item.get('formatted_date')
        events = fixture_item.get('events')

        fixture_object = FixtureList(venue,status,localteam_name,localteam_score,visitorteam_name,visitorteam_score,time,formatted_date,events)
        fixture_results.append(fixture_object)
    return fixture_results




def get_details(id):
    get_details_url=details_url.format(id,apikey)
    with urllib.request.urlopen(get_details_url) as url:
        get_detail_data=url.read()
        get_detail_response=json.loads(get_detail_data)
        details_result=None

        if get_detail_response:
            details_results_list=get_detail_response
            detail_results=process_details_results(details_results_list)
    return  detail_results


def process_details_results(detail_list):
    detail_results = []
    # print(detail_list.keys())
    # print(detail_list['lineup'])



    lineup= detail_list['lineup']
    subs = detail_list['subs']
    comments=detail_list['comments']
    stats=detail_list['match_stats']
    details_object = MatchDetails(lineup,subs,comments,stats)
    detail_results.append(details_object)


    return  detail_results
