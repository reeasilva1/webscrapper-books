from bs4 import BeautifulSoup

def parse_books(html: str) -> list[dict]:
    """Extrai título, preço e disponibilidade dos livros."""
    soup = BeautifulSoup(html, "html.parser")
    books = []

    for book in soup.select(".product_pod"):
        title = book.h3.a["title"]
        price = book.select_one(".price_color").get_text()
        availability = book.select_one(".availability").get_text(strip=True)

        books.append({
            "title": title,
            "price": price,
            "availability": availability
        })

    return books
