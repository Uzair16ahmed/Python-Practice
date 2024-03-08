import pandas as pd
import sys

def csv_to_excel(csv_file, excel_file):
    try:
        # Read CSV file into a DataFrame
        df = pd.read_csv(csv_file)
        print(df)
        # Export DataFrame to Excel file
        df.to_excel(excel_file, index=False)
        print(f"CSV file '{csv_file}' successfully converted to Excel file '{excel_file}'.")
    except Exception as e:
        print(f"Error converting CSV file '{csv_file}' to Excel file '{excel_file}': {e}")


if __name__ == "__main__":
    if len(sys.argv)!= 3:
        print("Usage: python csv_to_excel.py <csv_file> <excel_file>")
        sys.exit(1)
    else:
        csv_file = sys.argv[1]
        excel_file = sys.argv[2]
        csv_to_excel(csv_file, excel_file)