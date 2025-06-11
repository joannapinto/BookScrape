# Book Scraper Project

This project is designed to scrape book details from the website [Books to Scrape](http://books.toscrape.com). It collects data such as **Title**, **Price**, **Rating**, **Availability**, and **Product URL**, processes pagination to scrape all available books (\~1000 total), and saves the results into a structured CSV file (`books_data.csv`).

## Features

* **Scrapes Book Details**: Extracts **Title**, **Price**, **Rating**, **Availability**, and **Product URL**.
* **Handles Pagination**: Automatically navigates across multiple pages (\~50 pages with 20 books each).
* **Saves Data to CSV**: Stores the scraped data in a well-structured CSV file (`books_data.csv`).
* **Robust Error Handling**: Handles missing fields gracefully and manages HTTP errors (e.g., 404, 500).
* **Tested for Functionality**: Includes comprehensive test cases to validate the scraper’s performance.

## Setup

### Prerequisites

1. Ensure **Python 3.6+** is installed on your system.
2. Install **Git** if you plan to clone the repository.

### Steps

1. **Clone or Navigate to the Project Directory**:

   ```bash
   git clone https://github.com/your-repo/book-scraper.git
   cd book-scraper
   ```

2. **Set Up a Virtual Environment (Recommended)**:

    **Windows**:

     ```bash
     python -m venv .venv
     .\.venv\Scripts\activate
     ```
    **macOS/Linux**:

     ```bash
     python -m venv .venv
     source .venv/bin/activate
     ```

3. **Install Dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Running the Scraper

Execute the script to scrape book data and save it to `books_data.csv`:

```bash
python scraper.py
```

### Running Tests

Validate the scraper's functionality with automated test cases:

```bash
pytest test_scraper.py
```

## Output

The scraper saves data into a CSV file named `books_data.csv` with the following columns:

| **Column Name**  | **Description**                     |
| ---------------- | ----------------------------------- |
| **Title**        | Name of the book                    |
| **Price**        | Price of the book (e.g., £51.77)    |
| **Rating**       | Book rating (e.g., One, Two, Three) |
| **Availability** | Whether the book is in stock        |
| **URL**          | Link to the book's product page     |

### Sample CSV Output

| Title                | Price  | Rating | Availability | URL                                                                             |
| -------------------- | ------ | ------ | ------------ | ------------------------------------------------------------------------------- |
| A Light in the Attic | £51.77 | Three  | In stock     | [http://books.toscrape.com/catalogue/](http://books.toscrape.com/catalogue/)... |
| Tipping the Velvet   | £53.74 | One    | In stock     | [http://books.toscrape.com/catalogue/](http://books.toscrape.com/catalogue/)... |
| Soumission           | £50.10 | Four   | Out of stock | [http://books.toscrape.com/catalogue/](http://books.toscrape.com/catalogue/)... |
| ...                  | ...    | ...    | ...          | ...                                                                             |

## Code Documentation

The project consists of two main functions and a driver script:

### 1. **`scrape_books` Function**

* **Purpose**: Scrapes book details (Title, Price, Rating, Availability, and URL) from all pages.
* **Handles**:

  * Pagination automatically.
  * Missing fields with error logging.

### 2. **`save_to_csv` Function**

* **Purpose**: Saves the scraped book data into a CSV file.
* **Ensures**:

  * Proper column structure (Title, Price, Rating, Availability, URL).
  * Encoding is set to `utf-8-sig` to handle special characters.

### 3. **Driver Script (\`if **name** == "**main**")**

* Combines the scraping and saving processes.
* Manages error handling for HTTP requests.

### Example Code Snippets

#### Scraping Books

```python
for book in book_list:
    title = book.h3.a['title']
    price = book.select_one('.price_color').text.strip()
    rating = book.select_one('.star-rating')['class'][1]
    availability = book.select_one('.availability').text.strip()
    product_url = f"{BASE_URL}{book.h3.a['href']}"
```

#### Saving Data

```python
def save_to_csv(data, filename='books_data.csv'):
    df = pd.DataFrame(data)
    df.to_csv(filename, index=False, encoding='utf-8-sig')
    print(f"Data saved to {filename}")
```

## Testing

The project includes comprehensive test cases (`test_scraper.py`) to validate:

| **Test Case**                     | **Description**                                               |
| --------------------------------- | ------------------------------------------------------------- |
| **CSV File Download**             | Ensures the file is created successfully.                     |
| **CSV File Extraction**           | Verifies the file content matches the scraped data.           |
| **File Type and Format**          | Ensures the CSV structure is valid.                           |
| **Data Structure Validation**     | Confirms all required fields are present in the scraped data. |
| **Handling Missing/Invalid Data** | Tests for graceful handling of missing or invalid fields.     |

Run the tests:

```bash
pytest test_scraper.py
```

Expected Output:
All tests completed successfully. No errors found.


## Additional Notes

* Confirm the `Books to Scrape` website is accessible during scraping.
* If issues occur, verify Python installation and dependencies.
* You can enhance the scraper to store data in a database for advanced use cases.


