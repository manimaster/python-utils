"""
URL Shortener

This script shortens a URL using Python and the 'tinyurl' library.
"""

import pyshorteners

def shorten_url(url):
    s = pyshorteners.Shortener()
    return s.tinyurl.short(url)

url_input = input("Enter URL to shorten: ")
print("Shortened URL:", shorten_url(url_input))
