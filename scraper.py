import requests
from bs4 import BeautifulSoup
import pandas as pd

# Base URL of the website
BASE_URL = "http://books.toscrape.com/"

def scrape_books():
    """Scrapes book details from all pages of the Books to Scrape website."""
    books = []
    next_page = "catalogue/page-1.html"  # Start with the first page

    while next_page:
        print(f"Scraping page: {BASE_URL}{next_page}")
        
        # Fetch the page content
        try:
            response = requests.get(f"{BASE_URL}{next_page}", timeout=10)
            response.raise_for_status()  # Raise an error for HTTP errors
        except requests.exceptions.RequestException as e:
            print(f"Error fetching page {next_page}: {e}")
            break

        # Parse the HTML content
        soup = BeautifulSoup(response.text, 'html.parser')
        book_list = soup.select('.product_pod')  # Select all book entries

        # Extract details of each book
        for book in book_list:
            try:
                title = book.h3.a['title']
                price = book.select_one('.price_color').text.strip()
                rating = book.select_one('.star-rating')['class'][1]
                availability = book.select_one('.availability').text.strip()
                product_url = f"{BASE_URL}{book.h3.a['href']}"

                books.append({
                    "Title": title,
                    "Price": price,
                    "Rating": rating,
                    "Availability": availability,
                    "URL": product_url
                })
            except AttributeError as e:
                print(f"Skipping book due to missing field: {e}")

        # Handle pagination: find the next page
        next_button = soup.select_one('.next a')
        if next_button:
            next_page = next_button['href']
            next_page = f"catalogue/{next_page}"  # Ensure relative URLs work correctly
        else:
            next_page = None  # End the loop if no "next" button is found

    return books

def save_to_csv(data, filename='books_data.csv'):
    """Saves the scraped book data to a CSV file."""
    df = pd.DataFrame(data)
    df.to_csv(filename, index=False, encoding='utf-8-sig')  # Handle special characters
    print(f"Data saved to {filename}")

if __name__ == "__main__":
    print("Scraping books from the website...")
    books_data = scrape_books()
    if books_data:
        save_to_csv(books_data)
    print("Scraping completed!")
