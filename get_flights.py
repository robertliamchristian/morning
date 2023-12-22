import requests
import json

# Your API request
url = "https://priceline-com-provider.p.rapidapi.com/v2/flight/roundTrip"
querystring = {"departure_date":"2024-01-05","adults":"1","sid":"iSiX639","results_per_page":"10","origin_airport_code":"PDX","destination_airport_code":"NYC"}
headers = {
    "X-RapidAPI-Key": "d49e56dcbemsh75dcc891664b5a7p1cb502jsnaab489024d84",
    "X-RapidAPI-Host": "priceline-com-provider.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)
data = response.json()

# Accessing the necessary data
results = data.get('getAirFlightRoundTrip', {}).get('results', {})
result = results.get('result', {})
itinerary_data = result.get('itinerary_data', {})
search_data = result.get('search_data', {}).get('search_0', {})

# Extract origin, destination, and departure date
origin = search_data.get('origin', {}).get('code', 'Unknown')
destination = search_data.get('destination', {}).get('code', 'Unknown')
departure_date = search_data.get('departure_date', 'Unknown')

# Loop through each itinerary
for key, itinerary in itinerary_data.items():
    # Assuming the fare is stored under 'display_total_fare_per_ticket'
    total_fare = itinerary.get('price_details', {}).get('display_total_fare_per_ticket', 'Unknown')

    # Print the extracted information
    print(f"Itinerary {key}:")
    print(f"Origin: {origin}, Destination: {destination}, Departure Date: {departure_date}")
    print(f"Total Fare: ${total_fare}")
    print("-" * 30)
