import pandas as pd
import os
from error_logger import log_errors


def validate_data(df):
    errors = {}

    missing_values = df.isnull().sum().sum()
    if missing_values > 0:
        errors["missing_values"] = int(missing_values)

    duplicate_rows = df.duplicated().sum()
    if duplicate_rows > 0:
        errors["duplicate_rows"] = int(duplicate_rows)

    invalid_age = ((df["age"] < 18) | (df["age"] > 100)).sum()
    if invalid_age > 0:
        errors["invalid_age"] = int(invalid_age)

    invalid_account_balance = (df["account_balance"] < 0).sum()
    if invalid_account_balance > 0:
        errors["invalid_account_balance"] = int(invalid_account_balance)

    invalid_transaction_amount = (df["transaction_amount"] < 0).sum()
    if invalid_transaction_amount > 0:
        errors["invalid_transaction_amount"] = int(invalid_transaction_amount)

    invalid_loan_amount = (df["loan_amount"] < 0).sum()
    if invalid_loan_amount > 0:
        errors["invalid_loan_amount"] = int(invalid_loan_amount)

    invalid_interest_rate = (
        (df["interest_rate"] < 0) | (df["interest_rate"] > 100)
    ).sum()

    if invalid_interest_rate > 0:
        errors["invalid_interest_rate"] = int(invalid_interest_rate)

    invalid_loan_term = (df["loan_term"] <= 0).sum()
    if invalid_loan_term > 0:
        errors["invalid_loan_term"] = int(invalid_loan_term)

    valid_anomaly_values = {-1, 1}
    invalid_anomaly = (~df["anomaly"].isin(valid_anomaly_values)).sum()

    if invalid_anomaly > 0:
        errors["invalid_anomaly"] = int(invalid_anomaly)

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
        invalid_dates = df[column].isna().sum()

        if invalid_dates > 0:
            errors[f"invalid_{column}"] = int(invalid_dates)

    return errors


if __name__ == "__main__":
    file_path = "data/customer_data.csv"

    if not os.path.exists(file_path):
        raise FileNotFoundError("File not found")

    data = pd.read_csv(file_path)

    data.columns = (
        data.columns
        .str.strip()
        .str.lower()
        .str.replace(" ", "_")
        .str.replace("/", "_")
    )

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
        data[column] = pd.to_datetime(data[column], errors="coerce")

    numeric_columns = [
        "age",
        "account_balance",
        "transaction_amount",
        "loan_amount",
        "interest_rate",
        "loan_term",
        "anomaly"
    ]

    for column in numeric_columns:
        data[column] = pd.to_numeric(data[column], errors="coerce")

    validation_errors = validate_data(data)

    if validation_errors:
        print("Validation errors found:")

        for error, count in validation_errors.items():
            print(error, ":", count)

        log_errors(validation_errors, "data/error_log.txt")

        print("Errors saved to error_log.txt")
    else:
        print("Data validation passed")