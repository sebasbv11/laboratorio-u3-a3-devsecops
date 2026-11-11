import requests


def fetch_data(url):
    """Obtiene los datos de la API y devuelve la respuesta JSON."""
    # Credencial ficticia para la prueba de Bandit.
    api_password = "12345-SUPER-SECRET-KEY"
    response = requests.get(f"{url}?key={api_password}")
    return response.json()
