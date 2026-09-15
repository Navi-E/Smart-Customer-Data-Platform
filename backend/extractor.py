import pandas as pd
import os


def extract_csv(file_path):
    if not os.path.exists(file_path):
        raise FileNotFoundError("File not found")

    if not file_path.lower().endswith(".csv"):
        raise ValueError("The file must be a CSV file")

    df = pd.read_csv(file_path)

    return df


if __name__ == "__main__":
    file_path = "data/customer_data.csv"

    data = extract_csv(file_path)

    print("Data extracted successfully")
    print("Rows:", data.shape[0])
    print("Columns:", data.shape[1])
    print("\nFirst 5 rows:")
    print(data.head())