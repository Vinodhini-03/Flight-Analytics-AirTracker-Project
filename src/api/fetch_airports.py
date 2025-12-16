import os
import requests
from dotenv import load_dotenv
from pathlib import Path

# Load .env explicitly
env_path = Path(__file__).resolve().parents[2] / ".env"
load_dotenv(dotenv_path=env_path, override=True)

print("ENV PATH CHECK:", env_path)

# ✅ Correct variable names
API_KEY = os.getenv("API_KEY")
API_HOST = os.getenv("API_HOST")

def fetch_airport(iata_code):
    url = f"https://{API_HOST}/airports/iata/{iata_code}"
    headers = {
        "x-rapidapi-key": API_KEY,
        "x-rapidapi-host": API_HOST
    }

    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json()

if __name__ == "__main__":
    print("API_HOST =", API_HOST)
    print("API_KEY =", API_KEY[:5], "...")
    print(fetch_airport("DEL"))
