import requests
import pandas as pd
import datetime

def fetch_football_predictions(football_api_key):
    today_date = datetime.datetime.now().date().isoformat()
    url = "https://football-prediction-api.p.rapidapi.com/api/v2/predictions"
    querystring = {"iso_date": today_date, "market": "classic"}
    headers = {
        "X-RapidAPI-Key": football_api_key,
        "X-RapidAPI-Host": "football-prediction-api.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)
    data = response.json()['data']
    print("Football API Response:", data)
    df = pd.DataFrame([{
        'Home Team': match['home_team'],
        'Away Team': match['away_team'],
        'competition_name': match['competition_name'],
        'Status': match['status'],
        'Result': match['result'],
        'Start Date': match['start_date'],
        'Odds 1': match['odds'].get('1'),
        'Odds X': match['odds'].get('X'),
        'Odds 2': match['odds'].get('2'),
    } for match in data])
    distinct_competitions = df['competition_name'].unique()
    for competition in distinct_competitions:
        print(competition)
    return df

fetch_football_predictions('d49e56dcbemsh75dcc891664b5a7p1cb502jsnaab489024d84')