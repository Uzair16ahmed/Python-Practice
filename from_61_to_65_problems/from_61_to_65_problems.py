import os
import urllib.request
import re

""" Problem 61: Write a program to print directory tree. The program should take path of a directory as argument
and print all the files in it recursively as a tree. """

# def tree(dir):
#     for root, dirs, files in os.walk(dir):
#         for file in files:
#             print(os.path.join(root,file))

def print_root_dir(path, indent=''):
    #  Print the current directory
    print(indent + os.path.basename(path)+ "/")

    # Check if the path is a directory
    if os.path.isdir(path):
        # List all files and directories in the current directory
        files = os.listdir(path)

        # Sort the files and directories
        files.sort()

        # Iterate through each file or directory
        for index, file in enumerate(files):
            # Construct the full path
            full_path = os.path.join(path, file)

            # Check if it's a directory
            if os.path.isdir(full_path):
                # If it's the last directory, modify the branch character
                if index == len(files) - 1:
                    print_root_dir(full_path, indent + '    ')
                else:
                    print_root_dir(full_path, indent + '|   ')
            else:
                # If it's the last file, modify the branch character
                if index == len(files) - 1:
                    print(indent + '\-- ' + file)
                else:
                    print(indent + '|-- ' + file)
    else:
        print("Not a directory")

"""     # check if the path is directory
    if os.path.isdir(path):
        # print all files and directories in the current directory
        files = os.listdir(path)

        # Sort the files and directories
        files.sort()

        # Iterate through each file or directory
        for file in files:
            # construct the full path
            full_path = os.path.join(path,file)

            # check if its a directory
            if os.path.isdir(full_path):
                print_root_dir(full_path, indent + '')
            else:
                print(indent + '|' + file) """




path = './'

# print_root_dir(path)
# tree(path)


""" "urllib module"
The urllib module provides functionality to download webpages. 

"""

response = urllib.request.urlopen("http://python.org/")
content = response.read()
# print(response.headers())
# print(response.headers['Content_Type'])
# print(content)

""" Problem 62: Write a program wget.py to download a given URL. The program should accept a URL as argument,
download it and save it with the basename of the URL. If the URL ends with a /, consider the basename as
index.html.
 """
""" 
import urllib.request
import urllib.parse
import os
import sys



def wget(url):
    try:
        # Encode the URL
        encoded_url = urllib.parse.quote(url, safe=':/')

        # Open the URL
        with urllib.request.urlopen(encoded_url) as response:
        # with urllib.request.urlopen(url) as response:

            filename = url.split('/')[-1]

            if filename == '':
                filename = 'index.html'
            
            with open(filename, 'wb') as file:
                file.write(response.read())

        print(f"Download {url} as {filename}")
    except Exception as e:
        print(f"Error downloading {url}: {e}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python wget.py <URL>")
        sys.exit(1)

    url = sys.argv[1]
    wget(url)

""" 
# output

#  PS F:\Python Practice\from_61_to_65_problems> python wget.py "https://www.pandasnovel.com/content/another-stupid-isekai(1)-1252-853008/chapter-23"
# Error downloading https://www.pandasnovel.com/content/another-stupid-isekai(1)-1252-853008/chapter-23: HTTP Error 403: Forbidden
# PS F:\Python Practice\from_61_to_65_problems> python wget.py "https://www.pandasnovel.com/content/another-stupid-isekai"
# Error downloading https://www.pandasnovel.com/content/another-stupid-isekai: HTTP Error 403: Forbidden

"""
 """

""" re module """

""" Problem 63: Write a program antihtml.py that takes a URL as argument, downloads the html from web and print
it after stripping html tags. """


""" 
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
            
"""

""" Problem 64: Write a function make_slug that takes a name converts it into a slug. A slug is a string where spaces
and special characters are replaced by a hyphen, typically used to create blog post URL from post title. It should
also make sure there are no more than one hyphen in any place and there are no hyphens at the beginning and end
of the slug """

def make_slug(name):
    slug = name.lower().replace(' ','-')
    # Remove special characters except hyphen and alphanumeric characters
    slug = re.sub(r'[^a-zA-Z0-9\-]', '', slug)
    # Remove consecutive hyphens
    slug = re.sub(r'[-]+', '-', slug)
    # Remove hyphens at the beginning and end of the slug
    slug = slug.strip('-')
    return slug

# print(make_slug("hello woRLd"))
# print(make_slug("hello woRLd!"))
# print(make_slug("---hello-  woRLd--"))


""" 
Problem 65: Write a program links.py that takes URL of a webpage as argument and prints all the URLs linked
from that webpage.
 """

""" 
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
         """