import sys

def main(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        file.close()

    for line in reversed(lines):
        print(line.strip())


if __name__ == "__main__":
    filename = sys.argv[1]
    main(filename)