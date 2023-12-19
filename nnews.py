import requests
import pandas as pd
import datetime

url = "https://news-api14.p.rapidapi.com/search"

querystring = {"q":"computer","country":"us","language":"en","pageSize":"10","publisher":"cnn.com,bbc.com"}

headers = {
    "X-RapidAPI-Key": "d49e56dcbemsh75dcc891664b5a7p1cb502jsnaab489024d84",
    "X-RapidAPI-Host": "news-api14.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

data = response.json()

print(data)  # Print the JSON response

# df = pd.DataFrame(data)
# print(df)