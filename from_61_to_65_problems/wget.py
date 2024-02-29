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

""" output

 PS F:\Python Practice\from_61_to_65_problems> python wget.py "https://www.pandasnovel.com/content/another-stupid-isekai(1)-1252-853008/chapter-23"
Error downloading https://www.pandasnovel.com/content/another-stupid-isekai(1)-1252-853008/chapter-23: HTTP Error 403: Forbidden
PS F:\Python Practice\from_61_to_65_problems> python wget.py "https://www.pandasnovel.com/content/another-stupid-isekai"
Error downloading https://www.pandasnovel.com/content/another-stupid-isekai: HTTP Error 403: Forbidden

"""