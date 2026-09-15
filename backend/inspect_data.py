import pandas as pd

file_path = "data/customer_data.csv"

df = pd.read_csv(file_path)

print("Rows:", df.shape[0])
print("Columns:", df.shape[1])

print("\nData types:")
print(df.dtypes)

missing = df.isnull().sum()
print("\nMissing values:")
print(missing[missing > 0])

print("\nDuplicate rows:", df.duplicated().sum())

print("\nUnique values:")
for column in df.columns:
    print(column, ":", df[column].nunique())

print("\nNumeric summary:")
print(df.describe())

print("\nFirst 5 rows:")
print(df.head())