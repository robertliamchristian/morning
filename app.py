from datetime import datetime
import requests
import pandas as pd

def fetch_weather(api_key, lat=45.52, lon=-122.68):
    # URL and parameters for OpenWeatherMap One Call API 3.0
    url = "https://api.openweathermap.org/data/3.0/onecall"
    params = {
        'lat': lat,
        'lon': lon,
        'appid': api_key,
        'units': 'imperial',  # For temperature in Fahrenheit
        'exclude': 'minutely,hourly,daily,alerts'  # Excluding parts not needed
    }

    # Making the API request
    response = requests.get(url, params=params)
    data = response.json()

    # Extracting data
    temp = data['current']['temp']
    feels_like = data['current']['feels_like']
    general_conditions = data['current']['weather'][0]['description']
    sunrise_time = datetime.fromtimestamp(data['current']['sunrise']).strftime('%H:%M')
    sunset_time = datetime.fromtimestamp(data['current']['sunset']).strftime('%H:%M')

    return temp, feels_like, general_conditions, sunrise_time, sunset_time

def fetch_football_predictions():
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

    return df

def morning_update_dates():
    today = datetime.now()
    today_formatted = today.strftime("%A, %B %d, %Y")

    new_years_day = datetime(today.year + 1, 1, 1)
    birthday = datetime(today.year, 2, 5)
    lindsay_birthday = datetime(today.year, 6, 6)

    if today > birthday:
        birthday = datetime(today.year + 1, 2, 5)
    if today > lindsay_birthday:
        lindsay_birthday = datetime(today.year + 1, 6, 6)

    days_until_new_years = (new_years_day - today).days
    days_until_birthday = (birthday - today).days
    days_until_lindsay_birthday = (lindsay_birthday - today).days

    return today_formatted, days_until_new_years, days_until_birthday, days_until_lindsay_birthday

def morning_update(api_key):
    # Fetch weather data
    temp, feels_like, general_conditions, sunrise, sunset = fetch_weather(api_key)

    # Fetch date information
    today_date, days_new_year, days_birthday, days_lindsay_birthday = morning_update_dates()

    # Fetch football predictions
    football_df = fetch_football_predictions()

    # Print the morning update
    print(f"Good morning Robbie\n\nToday's Date: {today_date}\n\nWeather today in Portland, OR:\nTemperature: {temp}°F\nFeels Like: {feels_like}°F\nConditions: {general_conditions}\nSunrise: {sunrise}\nSunset: {sunset}\n\nDays remaining until New Year's Day: {days_new_year}\nDays remaining until your birthday: {days_birthday}\nDays remaining until Lindsay's birthday: {days_lindsay_birthday}\n\nToday's Football Predictions:")
    print(football_df.to_string(index=False))

# Use your API key
api_key = '89fbedb87c83a9faf12a1319c4df142e'

# Call the function to display the morning update
morning_update(api_key)
