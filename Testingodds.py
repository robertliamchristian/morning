import pandas as pd
import requests
from datetime import datetime

# Get today's date in ISO format
today_date = datetime.now().date().isoformat()

# API request
url = "https://football-prediction-api.p.rapidapi.com/api/v2/predictions"
querystring = {"iso_date": today_date, "market": "classic"}
headers = {
    "X-RapidAPI-Key": "d49e56dcbemsh75dcc891664b5a7p1cb502jsnaab489024d84",
    "X-RapidAPI-Host": "football-prediction-api.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)
data = response.json()['data']

# Creating DataFrame
df = pd.DataFrame([{
    'Home Team': match['home_team'],
    'Away Team': match['away_team'],
    'Competition': match['competition_name'],
    'Status': match['status'],
    'Result': match['result'],
    'Start Date': match['start_date'],
    'Odds 1': match['odds'].get('1'),
    'Odds X': match['odds'].get('X'),
    'Odds 2': match['odds'].get('2'),
} for match in data])


pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns',None)
print(df)
