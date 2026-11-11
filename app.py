import requests
def fetch_data(url):
    """Obtiene los datos de la API y devuelve la respuesta JSON."""
    # Vulnerabilidad SAST: Uso de credenciales hardcodeadas
    api_key = "12345-SUPER-SECRET-KEY"
    response = requests.get(f"{url}?key={api_key}")
    return response.json()
