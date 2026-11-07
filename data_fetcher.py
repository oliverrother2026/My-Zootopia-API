import os
import requests
from dotenv import load_dotenv

load_dotenv(dotenv_path=".env", override=True)

API_KEY = os.getenv("API_KEY")
API_URL = "https://api.api-ninjas.com/v1/animals"


def fetch_data(animal_name):
    """
    Fetches animal data from the API.
    Returns a list of animal dictionaries.
    """
    response = requests.get(
        API_URL,
        headers={"X-Api-Key": API_KEY},
        params={"name": animal_name},
        timeout=10
    )

    response.raise_for_status()

    return response.json()