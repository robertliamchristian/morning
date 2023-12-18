import datetime
import pandas as pd
import requests

# Your API key
api_key = 'AIzaSyBfw_KuFQwYvCgIm9ZDdJGuvqAKUWzmw5Q'

# Your Calendar ID
calendar_id = 'robertliamchristian@gmail.com'

# URL for Google Calendar API
url = f"https://www.googleapis.com/calendar/v3/calendars/{calendar_id}/events"

# Get today's date range
today = datetime.date.today()
start_of_day = datetime.datetime.combine(today, datetime.time())
end_of_day = datetime.datetime.combine(today, datetime.time(23, 59, 59))

# Parameters for the API call
params = {
    'key': api_key,
    'timeMin': start_of_day.isoformat() + 'Z',
    'timeMax': end_of_day.isoformat() + 'Z',
    'singleEvents': True,
    'orderBy': 'startTime'
}

# Make the request
response = requests.get(url, params=params)
events = response.json().get('items', [])

# Extract event data
data = [{'Name': event['summary'], 
         'Start': event['start'].get('dateTime', event['start'].get('date')), 
         'End': event['end'].get('dateTime', event['end'].get('date'))} 
        for event in events]

# Create DataFrame
df = pd.DataFrame(data)
print(df)
