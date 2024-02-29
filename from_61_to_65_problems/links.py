import requests
from bs4 import BeautifulSoup
import sys
import re


def extract_links(url):
    try:
        # Fetch the HTML content of the webpage
        response = requests.get(url)
        html_content = response.text

        # Parse HTML using BeautifulSoup
        soup = BeautifulSoup(html_content, 'html.parser')

        # Find all anchor tags (<a>) containing href attribute
        links = soup.find_all('a', href=True)

        # Extract URLs from href attributes
        urls = [link['href'] for link in links]

        # Filter out URLs that are not absolute or start with 'http' or 'https'
        urls = [url for url in urls if url.startswith('http')]

        return urls

    except Exception as e:
        print(f"Error extracting links from {url}: {e}")
        return []



if __name__ == "__main__":
    # Check if URL argument is provided
    if len(sys.argv) != 2:
        print("Usage: python links.py <URL>")
        sys.exit(1)

    # Get URL from command line argument
    url = sys.argv[1]


    links = extract_links(url)

    if links:
        print(f"Found {len(links)} links in {url}")
        for link in links:
            print(link)
    else:
        print(f"No links found in {url}")