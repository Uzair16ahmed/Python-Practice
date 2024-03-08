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

"""
import zipfile
import sys
import os

def create_zip(zip_filename, files_to_add):
    try:
        with zipfile.ZipFile(zip_filename, 'w') as zipf:
            for file in files_to_add:
                if os.path.exists(file):
                    zipf.write(file, os.path.basename(file))
                else:
                    print(f"File not found:", {file})
    except Exception as e:
        print(f"Error creating zip file: {e}")


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python create_zip.py <zip_filename> <files_to_add>")
        sys.exit(1)
    else:
        zip_filename = sys.argv[1]
        files_to_add = sys.argv[2:]
        create_zip(zip_filename, files_to_add)
 
"""

""" Problem 69: Write a program mydoc.py to implement the functionality of pydoc. The program should take
the module name as argument and print documentation for the module and each of the functions defined in that
module """

""" 
import importlib
import inspect
import sys

def print_module_doc(module_name):
    try:
        module = importlib.import_module(module_name)
        print(f"Documentation for module:", {module_name})
        print(module.__doc__)
        print()

        functions = inspect.getmembers(module, inspect.isfunction)
        for name, function in functions:
            print(f"Documentation for function:", {name})
            print(function.__doc__)
            print()

    except ImportError:
        print(f"Module '{module_name}' not found.")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python print_module_doc.py <module_name>")
        sys.exit()
    else:
        module_name = sys.argv[1]
        print_module_doc(module_name)

"""


"""                 Installing third-party modules

PyPI, The Python Package Index maintains the list of Python packages available.
The third-party module developers usually register at PyPI and uploads their packages there. 

"""


""" Problem 70: Write a program csv2xls.py that reads a csv file and exports it as Excel file. The prigram should
take two arguments. The name of the csv file to read as first argument and the name of the Excel file to write as
the second argument. 
"""

""" import pandas as pd
import sys

def csv_to_excel(csv_file, excel_file):
    try:
        # Read CSV file into a DataFrame
        df = pd.read_csv(csv_file)
        print(df)
        # Export DataFrame to Excel file
        df.to_excel(excel_file, index=False)
        print(f"CSV file '{csv_file}' successfully converted to Excel file '{excel_file}'.")
    except Exception as e:
        print(f"Error converting CSV file '{csv_file}' to Excel file '{excel_file}': {e}")


if __name__ == "__main__":
    if len(sys.argv)!= 3:
        print("Usage: python csv_to_excel.py <csv_file> <excel_file>")
        sys.exit(1)
    else:
        csv_file = sys.argv[1]
        excel_file = sys.argv[2]
        csv_to_excel(csv_file, excel_file) """