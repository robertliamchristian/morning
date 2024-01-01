import datetime
import requests
import pandas as pd
from jinja2 import Environment, FileSystemLoader
import random
import datetime
from datetime import datetime as dt
from pytz import timezone

# Pulls odds data from API
def fetch_odds(api_key, date):
    """Fetch odds data for a given date."""
    url = "https://api-football-v1.p.rapidapi.com/v3/odds"
    headers = {
        "X-RapidAPI-Key": api_key,
        "X-RapidAPI-Host": "api-football-v1.p.rapidapi.com"
    }
    querystring = {"date": date}
    response = requests.get(url, headers=headers, params=querystring)
    return response.json()

# Pulls fixtures data from API
def fetch_fixtures(api_key, date):
    """Fetch fixtures data for a given date."""
    url = "https://api-football-v1.p.rapidapi.com/v3/fixtures"
    headers = {
        "X-RapidAPI-Key": api_key,
        "X-RapidAPI-Host": "api-football-v1.p.rapidapi.com"
    }
    querystring = {"date": date}
    response = requests.get(url, headers=headers, params=querystring)
    return response.json()



# Itterates through Odds data to find specific odds in nested keys
def extract_odds(bookmakers, bet_name="Match Winner"):
    """Extracts odds for Home, Draw, and Away from the bookmakers data."""
    for bookmaker in bookmakers:
        for bet in bookmaker['bets']:
            if bet['name'] == bet_name:
                odds = {value['value']: value['odd'] for value in bet['values']}
                return odds.get("Home"), odds.get("Draw"), odds.get("Away")
    return None, None, None

# Itterates through processed odds data and then appanends to df fixture id
def extract_odds_data(odds_data):
    """Extract odds and fixture ID from the odds data."""
    extracted_data = []
    for item in odds_data.get('response', []):
        fixture_id = item['fixture']['id']
        home_odds, draw_odds, away_odds = extract_odds(item.get('bookmakers', []))
        if home_odds and draw_odds and away_odds:
            extracted_data.append({'fixture_id': fixture_id, 'home_odds': home_odds, 'draw_odds': draw_odds, 'away_odds': away_odds})
    return extracted_data


def extract_fixtures_data(fixtures_data):
    """Extracts teams, league, and fixture ID from fixtures data."""
    extracted_data = []
    for item in fixtures_data.get('response', []):
        fixture_id = item['fixture']['id']
        home_team = item['teams']['home']['name']
        away_team = item['teams']['away']['name']
        league_name = item['league']['name']
        date = item['fixture']['date']

        # Convert the date to Pacific Time
        date = pd.to_datetime(date).tz_convert('US/Pacific')

        extracted_data.append({'fixture_id': fixture_id, 'date': date, 'home_team': home_team, 'away_team': away_team, 'league_name': league_name})
    return extracted_data
    
def fetch_football_odds(api_key, date=dt.now().strftime("%Y-%m-%d")):
    # Fetch odds data
    odds_data = fetch_odds(api_key, date)
    print(odds_data)
    # Fetch fixtures data
    fixtures_data = fetch_fixtures(api_key, date)
    print(fixtures_data)

    # Extract relevant data from odds and fixtures
    odds_extracted = extract_odds_data(odds_data)
    print(odds_extracted)
    fixtures_extracted = extract_fixtures_data(fixtures_data)
    print(fixtures_extracted)
    # Convert to DataFrames
    odds_df = pd.DataFrame(odds_extracted)
    fixtures_df = pd.DataFrame(fixtures_extracted)

    # Merge DataFrames on fixture_id
    merged_df = pd.merge(fixtures_df, odds_df, on='fixture_id')

    # Format final DataFrame
    final_df = merged_df[['date', 'home_team', 'away_team', 'league_name', 'home_odds', 'draw_odds', 'away_odds']]
    final_df['Match'] = final_df['home_team'] + ' vs ' + final_df['away_team']
    final_df = final_df[['date', 'Match', 'league_name', 'home_odds', 'draw_odds', 'away_odds']]

    return final_df



