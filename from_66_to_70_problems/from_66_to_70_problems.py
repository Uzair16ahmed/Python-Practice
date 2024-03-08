import re
import json
import zipfile
""" Problem 66: Write a regular expression to validate a phone number.
"""

def validate_phone(phone):
    # pattern = r'^\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}$'
    pattern = r'^\+\d{2}\s\d{3}-\d{7}$'
    return bool(re.match(pattern, phone))

# test cases

phone_numbers = [
    "(123) 456-7890",
    "123-456-7890",
    "123.456.7890",
    "1234567890",
    "(123)456-7890",
    "123 456 7890",
    "12345678901234", # This should fail, too many digits
    "+92 222-5555555",
    "+92 2225555555",
    "+92222-5555555", # This should fail, incorrect format
    "+92 222-55555555" # This should fail, too many digits
]

# for number in phone_numbers:
    # print(f"{number}: {validate_phone(number)}")


""" json module """

""" Problem 67: Write a program myip.py to print the external IP address of the machine. Use the response from
http://httpbin.org/get and read the IP address from there. The program should print only the IP address
and nothing else.
 """

"""
import json
import requests


def get_external_ip():
    try:
        response = requests.get('http://httpbin.org/get')
        data = response.json()
        print('data from response json', data)
        ip_address = data['origin']
        return ip_address
    except Exception as e:
        print(f"An error occured: {e}")
        return None


if __name__ == "__main__":
    ip_address = get_external_ip()
    if ip_address:
        print(ip_address)
    
"""

""" zipfile module """

""" The zipfile module provides interface to read and write zip files. """

z = zipfile.ZipFile("from_66_to_70_problems/NotePad Information.zip")
# for name in z.namelist():
    # print("File: ",name)
    # print(z.read(name))


""" Problem 68: Write a python program zip.py to create a zip file. The program should take name of zip file as first
argument and files to add as rest of the arguments. """