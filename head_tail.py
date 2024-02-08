import sys

def head(filename):
    with open(filename, 'r') as file:
        for i, line in enumerate(file):
            if i >= 10:
                break
            print(line.strip())

def tail(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()

    for line in lines[-10:]:
        print(line.strip())

if __name__ == "__main__":
    filename = sys.argv[1]
    head(filename)
    print("space")
    tail(filename)