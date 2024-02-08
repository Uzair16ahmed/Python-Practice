import sys

def main(filename):
    with open(filename, 'r') as file:

        for line in file:
            print(line.strip()[::-1])


if __name__ == "__main__":
    filename = sys.argv[1]
    main(filename)