import pytest
from scraper import scrape_books, save_to_csv
import os
import pandas as pd
from io import StringIO
import sys

def test_scrape_books():
    """
    Test Case 1: Verify CSV File Download
    Ensures that at least one book is scraped and required fields are present.
    """
    books = scrape_books()
    assert len(books) > 0, "No books were scraped"
    assert "Title" in books[0], "Missing Title field"
    assert "Price" in books[0], "Missing Price field"

def test_save_to_csv():
    """
    Test Case 2: Verify CSV File Extraction
    Ensures that a CSV file is generated with expected content.
    """
    test_data = [{"Title": "Sample", "Price": "£50", "Rating": "Five", "Availability": "In stock", "URL": "http://example.com"}]
    filename = "test_books_data.csv"
    save_to_csv(test_data, filename)
    
    # Verify file existence
    assert os.path.exists(filename), "CSV file was not created"
    
    # Verify content
    with open(filename, encoding="utf-8-sig") as file:
        content = file.read()
    assert "Sample" in content, "CSV file does not contain expected content"

    # Cleanup
    os.remove(filename)

def test_csv_format():
    """
    Test Case 3: Validate File Type and Format
    Ensures that the saved file is a valid CSV with correct columns.
    """
    test_data = [{"Title": "Sample", "Price": "£50", "Rating": "Five", "Availability": "In stock", "URL": "http://example.com"}]
    filename = "test_books_data_format.csv"
    save_to_csv(test_data, filename)
    
    # Load the CSV and validate structure
    df = pd.read_csv(filename)
    assert list(df.columns) == ["Title", "Price", "Rating", "Availability", "URL"], "CSV file structure is incorrect"
    
    # Cleanup
    os.remove(filename)

def test_data_structure():
    """
    Test Case 4: Validate Data Structure
    Ensures that all required fields are present in the scraped data.
    """
    books = scrape_books()
    for book in books:
        assert "Title" in book, "Missing Title field"
        assert "Price" in book, "Missing Price field"
        assert "Rating" in book, "Missing Rating field"
        assert "Availability" in book, "Missing Availability field"
        assert "URL" in book, "Missing URL field"

def test_handle_missing_data():
    """
    Test Case 5: Handle Missing or Invalid Data
    Ensures that the scraper handles missing fields gracefully and skips invalid data.
    """
    books = scrape_books()
    for book in books:
        assert book.get("Title") is not None, "Title field is missing or invalid"
        assert book.get("Price") is not None, "Price field is missing or invalid"
        assert book.get("Rating") is not None, "Rating field is missing or invalid"
        assert book.get("Availability") is not None, "Availability field is missing or invalid"
        assert book.get("URL") is not None, "URL field is missing or invalid"

if __name__ == "__main__":
    # Suppress unnecessary logs
    old_stdout = sys.stdout
    sys.stdout = StringIO()  # Redirect stdout to suppress output

    try:
        # Run all tests
        test_scrape_books()
        test_save_to_csv()
        test_csv_format()
        test_data_structure()
        test_handle_missing_data()

        # Restore stdout and print success message
        sys.stdout = old_stdout
        print("All tests completed successfully. No errors found.")
    except AssertionError as e:
        sys.stdout = old_stdout
        print(f"Test failed: {e}")
