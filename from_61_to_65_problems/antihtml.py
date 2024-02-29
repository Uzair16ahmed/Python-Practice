import urllib.request
import sys
from bs4 import BeautifulSoup

def fetch_html(url):
    try:
        with urllib.request.urlopen(url) as response:
            # Read the HTML content
            html_content = response.read()
        return html_content
    
    except Exception as e:
        print(f"Error fetching HTML from {url}: {e}")
        return None


def strip_html_tags(html_content):
    try:
        # Parse HTML using beautifulSoup
        soup = BeautifulSoup(html_content, 'html.parser')
        # Strip HTML tags
        text = soup.get_text(separator=' ')
        return text

    except Exception as e:
        print(f"Error stripping HTML tags: {e}")
        return None


if __name__ == "__main__":
    # check if url argument is provided
    if len(sys.argv)!= 2:
        print("Usage: python antihmtl.py <url>")
        sys.exit(1)

    # Get URL from command line argument
    url = sys.argv[1]

    # Fetch HTML content
    html_content = fetch_html(url)
    if html_content:
        # Strip HTML tags
        text = strip_html_tags(html_content)
        if text:
            print(text)