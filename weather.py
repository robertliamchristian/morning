import datetime
import requests
import pandas as pd
from jinja2 import Environment, FileSystemLoader
import random
import datetime
from datetime import datetime as dt


def fetch_weather(api_key, lat=45.52, lon=-122.68):
    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        'lat': lat,
        'lon': lon,
        'appid': api_key,
        'units': 'imperial'
    }
    response = requests.get(url, params=params)
    data = response.json()
    print("Weather API Response:", data)  # Debug print
    if 'main' in data and 'weather' in data:
        temp = data['main']['temp']
        weather_description = data['weather'][0]['description']
        # You need to add sunrise, sunset, temp_high, and temp_low here
        # If the API does not provide these directly, calculate or set defaults
        # For now, I'll set them to None
        temp_high = data['main'].get('temp_max', None)
        temp_low = data['main'].get('temp_min', None)
        # Convert Unix timestamps to human-readable times if available
       # Correct way to use fromtimestamp
        sunrise = datetime.datetime.fromtimestamp(data['sys']['sunrise']).strftime('%H:%M') if 'sys' in data else None
        sunset = datetime.datetime.fromtimestamp(data['sys']['sunset']).strftime('%H:%M') if 'sys' in data else None

        return temp, weather_description, temp_high, temp_low, sunrise, sunset
    else:
        print("Error fetching weather data")
        return None, None, None, None, None, None