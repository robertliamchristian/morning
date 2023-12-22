import requests
import json
import pandas as pd

def fetch_ny_flights():
    url = "https://priceline-com-provider.p.rapidapi.com/v2/flight/departures"
    querystring = {
        "departure_date":"2024-01-05",
        "sid":"iSiX639",
        "adults":"1",
        "page":"1",
        "results_per_page":"10",
        "number_of_itineraries":"10",
        "destination_city_id":"NYC",
        "origin_airport_code":"PDX"
    }
    headers = {
        "X-RapidAPI-Key": "d49e56dcbemsh75dcc891664b5a7p1cb502jsnaab489024d84",
        "X-RapidAPI-Host": "priceline-com-provider.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)
    data = response.json()

    results = data.get('getAirFlightDepartures', {}).get('results', {})
    result = results.get('result', {})
    search_data = result.get('search_data', {}).get('search_0', {})
    itinerary_data = result.get('itinerary_data', {})

    origin = search_data.get('origin', {}).get('code', 'Unknown')
    destination = search_data.get('destination', {}).get('code', 'Unknown')
    departure_date = search_data.get('departure_date', 'Unknown')

    flights = []

    for key, itinerary in itinerary_data.items():
        total_fare = itinerary.get('price_details', {}).get('display_total_fare_per_ticket', 'Unknown')
        flight_info = {
            "Itinerary": key,
            "Origin": origin,
            "Destination": destination,
            "Departure Date": departure_date,
            "Total Fare": total_fare
        }
        flights.append(flight_info)

    return pd.DataFrame(flights)
