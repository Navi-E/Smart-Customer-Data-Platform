import pandas as pd
import os


def transform_data(df):
    # Clean column names
    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(" ", "_")
        .str.replace("/", "_")
    )

    # Remove extra spaces from text values
    text_columns = df.select_dtypes(include="object").columns

    for column in text_columns:
        df[column] = df[column].str.strip()

    # Convert date columns
    date_columns = [
        "date_of_account_opening",
        "last_transaction_date",
        "transaction_date",
        "approval_rejection_date",
        "payment_due_date",
        "last_credit_card_payment_date",
        "feedback_date",
        "resolution_date"
    ]

    for column in date_columns:
        df[column] = pd.to_datetime(df[column], errors="coerce")

    # Convert numeric columns
    numeric_columns = [
        "age",
        "account_balance",
        "transaction_amount",
        "account_balance_after_transaction",
        "loan_amount",
        "interest_rate",
        "loan_term",
        "credit_limit",
        "credit_card_balance",
        "minimum_payment_due",
        "rewards_points",
        "anomaly"
    ]

    for column in numeric_columns:
        df[column] = pd.to_numeric(df[column], errors="coerce")

    return df


if __name__ == "__main__":
    file_path = "data/customer_data.csv"

    if not os.path.exists(file_path):
        raise FileNotFoundError("File not found")

    data = pd.read_csv(file_path)

    transformed_data = transform_data(data)

    print("Data transformed successfully")
    print("Rows:", transformed_data.shape[0])
    print("Columns:", transformed_data.shape[1])

    print("\nColumn names:")
    print(transformed_data.columns.tolist())

    print("\nData types:")
    print(transformed_data.dtypes)

    print("\nFirst 5 rows:")
    print(transformed_data.head())