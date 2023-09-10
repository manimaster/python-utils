"""
Simple Image Downloader

This script allows the user to download images from a provided URL.
"""

import os
import requests
from bs4 import BeautifulSoup

def download_images(url, folder):
    if not os.path.exists(folder):
        os.makedirs(folder)

    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    img_tags = soup.find_all('img')
    
    for img in img_tags:
        img_url = img.attrs.get('src')
        if img_url:
            if not img_url.startswith(('data:image', 'javascript')):
                img_name = os.path.join(folder, os.path.basename(img_url))
                with open(img_name, 'wb') as f:
                    f.write(requests.get(img_url).content)

url = input("Enter URL to scrape images: ")
download_images(url, 'downloaded_images')
