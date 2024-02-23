import os
import collections

def extCount(dirPath):
    extension_counts = collections.defaultdict(int)
    for root, _, files in os.walk(dirPath):
        for file in files:
            if file.endswith(".py"):
                _, extension = os.path.splitext(file)
                extension_counts[extension] += 1
                # print(os.path.join(root, file))
            elif file.endswith(".csv"):
                _, extension = os.path.splitext(file)
                extension_counts[extension] += 1
                # print(root, file)
                # print(os.path.join(root, file))
            elif file.endswith(".txt"):
                _, extension = os.path.splitext(file)
                extension_counts[extension] += 1
                # print(root, file)

    #  Print the count and extension for each available file extension
    for extension, count in extension_counts.items():
        print(f"{extension}: {count}")

def main():
    dirPath = './'
    extCount(dirPath)

if __name__ == "__main__":
    main()

# import os
# import collections
# import sys

# def count_extensions(directory):
#     # Create a dictionary to store counts of file extensions
#     extension_counts = collections.defaultdict(int)
#     print(extension_counts)
#     # Traverse the directory and count file extensions
#     for root, _, files in os.walk(directory):
#         for file in files:
#             _, extension = os.path.splitext(file)
#             extension_counts[extension] += 1

#     # Print the count and extension for each available file extension
#     for extension, count in extension_counts.items():
#         print(f"{extension}: {count}")

# if __name__ == "__main__":
#     # if len(sys.argv) != 2:
#     #     print("Usage: python extcount.py <directory>")
#     #     sys.exit(1)

#     directory = './PythonbyTraversyMedia'
#     count_extensions(directory)
