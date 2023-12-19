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

# API request
url = "https://api-football-v1.p.rapidapi.com/v3/odds"
# Getting today's date in the format YYYY-MM-DD
today_date = datetime.now().strftime("%Y-%m-%d")
querystring = {"date": today_date}
headers = {
    "X-RapidAPI-Key": "d49e56dcbemsh75dcc891664b5a7p1cb502jsnaab489024d84",
    "X-RapidAPI-Host": "api-football-v1.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)
data = response.json()

# Process the response
matches_data = []
for item in data.get('response', []):
    league = item.get('league', {})
    league_name = league.get('name')
    fixture = item.get('fixture', {})
    date = fixture.get('date')
    # Extracting home and away team names
    home_team = league.get('home', {}).get('name')
    away_team = league.get('away', {}).get('name')
    home_odds, draw_odds, away_odds = extract_odds(item.get('bookmakers', []))

    if home_odds and draw_odds and away_odds:
        matches_data.append([date, f"{home_team} vs {away_team}", league_name, home_odds, draw_odds, away_odds])

# Load into DataFrame
df = pd.DataFrame(matches_data, columns=['Date', 'Match', 'League', 'Home Odds', 'Draw Odds', 'Away Odds'])

# Print DataFrame
print(df)
