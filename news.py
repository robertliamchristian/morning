'''
def fetch_news_data():
    url = "https://newsnow.p.rapidapi.com/headline"
    payload = { "text": "United States" }
    headers = {
        "content-type": "application/json",
        "X-RapidAPI-Key": "d49e56dcbemsh75dcc891664b5a7p1cb502jsnaab489024d84",
        "X-RapidAPI-Host": "newsnow.p.rapidapi.com"
    }

    news_data = response.json()
    if isinstance(news_data, list):
        print("news_data is a list")

        # Check if the first item in the list is a dictionary
        if isinstance(news_data[0], dict):
            print("The first item in news_data is a dictionary")
    else:
        print("news_data is not a list")

    return news_data
'''