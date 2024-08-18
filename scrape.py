import requests
from bs4 import BeautifulSoup
import json
import os

def fetch_books(page_number):
    url = f"https://books.toscrape.com/catalogue/page-{page_number}.html"
    linkUrl = f"https://books.toscrape.com/catalogue/"
    baseUrl = f"https://books.toscrape.com/"
    books = []
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')

        # books elements
        book_elements = soup.find_all('article', class_='product_pod')

        # loops
        for book in book_elements:
            title = book.find('h3').find('a')['title']
            link_element = book.find('h3').find('a')['href']
            link = linkUrl + link_element
            price = book.find('p', class_='price_color').text.replace('Â', '')

            # image
            imageUrl = book.find('div', class_='image_container').find('a').find('img')['src']
            image = baseUrl + imageUrl
            # instock
            availability_text = book.find('p', class_='instock availability').text
            instock = 'In stock' if 'In stock' in availability_text else 'Out of stock'
            # rating
            rating_element = book.find('p', class_='star-rating')
            get_class_index_rating = rating_element['class'][1]


            books.append({
                "title": title,
                "price": price,
                "stock": instock,
                "rating": get_class_index_rating,
                "link": link,
                "image_url": image,
            });
            
        return books

    except Exception as e:
        print("🔥 🔥 🔥 🔥 🔥 Oops !!! : ", e)
    
def main():
    all_books = []
    max_pages = 3

    # data directory
    data_directory = "./data"

    for current_page in range(1, max_pages + 1):
        books_on_page = fetch_books(current_page)
        all_books.extend(books_on_page)
        print(f"Book on page {current_page} : {books_on_page}")

    # Create the directory if it doesn't exist
    os.makedirs(data_directory, exist_ok=True)
    
    # Save data to file
    with open(os.path.join(data_directory, 'books.json'), 'w') as f:
        json.dump(all_books, f, indent=2)

    print("Data saved to books.json file")


if __name__ == "__main__":
    main()