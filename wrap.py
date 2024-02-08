import sys

def wrap(filename, width):
    with open(filename, 'r') as file:
        lines = file.readlines()
    wrapped_lines = []

    for line in lines:
        while len(line) > width:
            wrapped_lines.append(line[:width])
            line = line[width:]
        wrapped_lines.append(line)

    for wrapped_line in wrapped_lines:
        print(wrapped_line.strip())

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python wrap.py <filename> <width>")
        sys.exit()
    
    filename = sys.argv[1]
    width = int(sys.argv[2])

    wrap(filename, width)