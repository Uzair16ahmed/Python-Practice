import sys

def grep(filename, string):
    with open(filename, 'r') as file:
        lines = file.readlines()
    for line in lines:
        if string in line:
            print(line.strip())

if __name__ == "__main__":
    filename = sys.argv[1]
    string = sys.argv[2]
    grep(filename, string)
