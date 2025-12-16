import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")
API_HOST = os.getenv("API_HOST")

HEADERS = {
    "x-rapidapi-key": API_KEY,
    "x-rapidapi-host": API_HOST
}

def fetch_flights(iata_code):
    url = f"https://{API_HOST}/airports/iata/{iata_code}/flights"
    params = {
        "offsetMinutes": -120,
        "durationMinutes": 240,
        "withCancelled": "true"
    }

    response = requests.get(url, headers=HEADERS, params=params)
    response.raise_for_status()
    return response.json()


if __name__ == "__main__":
    data = fetch_flights("DEL")
    print(data.keys())
    print(data.get("departures", [])[:1])
