from scraper import get_page, BASE_URL
from parser import parse_books
from utils import save_to_csv


BASE_URL = "https://books.toscrape.com/catalogue/page-{}.html"

def main():
    print("Iniciando WebScraper...")
    all_books = []

    for page in range(1,6):
        url = BASE_URL.format(page)
        try:
            html = get_page(url)
            books = parse_books(html)
            all_books.extend(books)
            print(f"Página {page}: {len(books)} livros coletados.")
        except Exception as e:
            print(f"Erro na pagina {page}: {e}")

    save_to_csv(all_books, "data/books.csv")

    print(f"{len(all_books)} livros salvos em data/books.csv")

if __name__ == "__main__":
    main()
