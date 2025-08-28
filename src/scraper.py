import requests

BASE_URL = "https://books.toscrape.com/"

def get_page(url: str) -> str:
    """Faz uma requisição HTTP e retorna o HTML da página."""
    response = requests.get(url)
    response.raise_for_status()  # dispara erro se der problema
    return response.text