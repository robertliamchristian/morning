import requests
import pandas as pd
from datetime import datetime


def extract_odds(bookmakers, bet_name="Match Winner"):
    """Extracts odds for Home, Draw, and Away from the bookmakers data."""
    for bookmaker in bookmakers:
        for bet in bookmaker['bets']:
            if bet['name'] == bet_name:
                odds = {value['value']: value['odd'] for value in bet['values']}
                return odds.get("Home"), odds.get("Draw"), odds.get("Away")
    return None, None, None

def extract_odds_data(odds_data):
    """Extract odds and fixture ID from the odds data."""
    extracted_data = []
    for item in odds_data.get('response', []):
        fixture_id = item['fixture']['id']
        home_odds, draw_odds, away_odds = extract_odds(item.get('bookmakers', []))
        if home_odds and draw_odds and away_odds:
            extracted_data.append({'fixture_id': fixture_id, 'home_odds': home_odds, 'draw_odds': draw_odds, 'away_odds': away_odds})
    return extracted_data

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

def extract_fixtures_data(fixtures_data):
    """Extracts teams, league, and fixture ID from fixtures data."""
    extracted_data = []
    for item in fixtures_data.get('response', []):
        fixture_id = item['fixture']['id']
        home_team = item['teams']['home']['name']
        away_team = item['teams']['away']['name']
        league_name = item['league']['name']
        date = item['fixture']['date']
        extracted_data.append({'fixture_id': fixture_id, 'date': date, 'home_team': home_team, 'away_team': away_team, 'league_name': league_name})
    return extracted_data

def main(api_key, date):
    # Fetch data from both APIs
    odds_data = fetch_odds(api_key, date)
    fixtures_data = fetch_fixtures(api_key, date)

    # Extract relevant data
    odds_extracted = extract_odds_data(odds_data)
    fixtures_extracted = extract_fixtures_data(fixtures_data)

    # Convert to DataFrames
    odds_df = pd.DataFrame(odds_extracted)
    fixtures_df = pd.DataFrame(fixtures_extracted)

    # Merge DataFrames on fixture_id
    merged_df = pd.merge(fixtures_df, odds_df, on='fixture_id')

    # Format final DataFrame
    final_df = merged_df[['date', 'home_team', 'away_team', 'league_name', 'home_odds', 'draw_odds', 'away_odds']]
    final_df['Match'] = final_df['home_team'] + ' vs ' + final_df['away_team']
    final_df = final_df[['date', 'Match', 'league_name', 'home_odds', 'draw_odds', 'away_odds']]

    # Set display option to show all columns
    pd.set_option('display.max_columns', None)

    print(final_df)

if __name__ == "__main__":
    api_key = "d49e56dcbemsh75dcc891664b5a7p1cb502jsnaab489024d84"
    today_date = datetime.now().strftime("%Y-%m-%d")
    main(api_key, today_date)
