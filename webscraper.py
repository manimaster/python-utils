"""
Web Scraper using BeautifulSoup

This script allows the user to scrape quotes from http://quotes.toscrape.com/
The scraped data includes the text of the quote, the author, and associated tags.
"""

import requests
from bs4 import BeautifulSoup

BASE_URL = "http://quotes.toscrape.com"

def get_quotes(page_number=1):
    response = requests.get(f"{BASE_URL}/page/{page_number}")
    soup = BeautifulSoup(response.content, "html.parser")
    
    quotes_divs = soup.find_all("div", class_="quote")
    
    for quote_div in quotes_divs:
        text = quote_div.find("span", class_="text").get_text()
        author = quote_div.find("small", class_="author").get_text()
        tags = [tag.get_text() for tag in quote_div.find_all("a", class_="tag")]
        
        print(f"Quote: {text}\nAuthor: {author}\nTags: {tags}\n\n")

get_quotes(1)
