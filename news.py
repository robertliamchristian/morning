import requests
import pandas as pd
url = "https://newsnow.p.rapidapi.com/newsv2"

payload = {
    "query": "AI",
    "page": 1,
    "time_bounded": False,
    "from_date": "12/15/2023",
    "to_date": "12/16/2023",
    "location": "",
    "category": "",
    "source": ""
}
headers = {
    "content-type": "application/json",
    "X-RapidAPI-Key": "d49e56dcbemsh75dcc891664b5a7p1cb502jsnaab489024d84",
    "X-RapidAPI-Host": "newsnow.p.rapidapi.com"
}

response = requests.post(url, json=payload, headers=headers)
data = response.json()

df = pd.DataFrame(data)
print(df)
