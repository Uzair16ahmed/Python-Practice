import sys

def wordwrap(text, width):
    words = text.split()
    lines = []
    current_line = words[0]

    for word in words[1:]:
        if len(current_line) + len(word) + 1 <= width:
            current_line += " " + word
        else:
            lines.append(current_line)
            current_line = word
    
    lines.append(current_line)
    return "\n".join(lines)

def main():
    if len(sys.argv) != 3:
        print("Usage: python wrap.py <filename> <width>")
        sys.exit()

    filename = sys.argv[1]
    width = int(sys.argv[2])

    with open(filename, 'r') as file:
        text = file.read()

    print(wordwrap(text, width))

if __name__ == "__main__":
    main()

"""
output:

She sells seashells on the
seashore; The shells that she
sells are seashells I'm sure.
So if she sells seashells on
the seashore, I'm sure that
the shells are seashore
shells. Sed ut perspiciatis
"""