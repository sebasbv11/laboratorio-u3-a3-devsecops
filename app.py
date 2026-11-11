import os

import requests


def fetch_data(url):
    """Obtiene los datos de la API y devuelve la respuesta JSON."""
    api_key = os.environ["API_KEY"]
    response = requests.get(url, params={"key": api_key}, timeout=10)
    response.raise_for_status()
    return response.json()
