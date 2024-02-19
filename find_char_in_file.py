import sys
import string

def count_char_frequency(filename):
    try:
        with open(filename, 'r') as file:
            text = file.read()
            frequency = {char: text.count(char) for char in set(text)}
            return frequency
    except FileNotFoundError:
        print("File not Found")
        return None

def identify_file_type(char_frequency):
    # We can make some assumptions based on character frequencies
    # to determine the file type.
    if '#' in char_frequency and char_frequency['#'] > 10:
        return " Python program file"
    elif ';' in char_frequency and char_frequency[';'] > 10:
        return " C program file"
    else: 
        return " Text file"


def main():
    if len(sys.argv) != 2:
        print("Usage: python identify_file_type.py <filename>")
        return 

    filename = sys.argv[1]
    char_frequency = count_char_frequency(filename)
    print(identify_file_type(char_frequency))

if __name__ == "__main__":
    main()