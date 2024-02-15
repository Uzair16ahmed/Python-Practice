import sys

def center_align(filename):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
            max_length = max(len(line.strip()) for line in lines)

            print("Center Aligned Text:")
            for line in lines:
                centered_line = line.strip().center(max_length)
                print(centered_line)

    except FileNotFoundError:
        print("File not Found")


def main():
    if len(sys.argv) != 2:
        print("Usage: python center_align.py <filename>")
        sys.exit()
    
    filename = sys.argv[1]

    center_align(filename)


if __name__ == "__main__":
    main()

"""
output:
                     She sells seashells on the seashore;
              The shells that she sells are seashells I'm sure.
                  So if she sells seashells on the seashore,
                I'm sure that the shells are seashore shells.
             Sed ut perspiciatis unde omnis iste natus error sit,
                voluptatem accusantium doloremque laudantium,

"""