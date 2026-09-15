import pandas as pd


def merge_data(dataframes):
    if not dataframes:
        raise ValueError("No data provided for merging")

    first_columns = list(dataframes[0].columns)

    for df in dataframes:
        if list(df.columns) != first_columns:
            raise ValueError("Dataframes have different columns")

    merged_data = pd.concat(dataframes, ignore_index=True)

    merged_data = merged_data.drop_duplicates()

    return merged_data


if __name__ == "__main__":
    data1 = pd.read_csv("data/customer_data.csv")
    data2 = pd.read_csv("data/customer_data.csv")

    merged_data = merge_data([data1, data2])

    print("Data merged successfully")
    print("Rows:", merged_data.shape[0])
    print("Columns:", merged_data.shape[1])