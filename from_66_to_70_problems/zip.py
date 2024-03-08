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
