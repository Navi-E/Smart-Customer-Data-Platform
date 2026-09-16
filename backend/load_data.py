import pandas as pd
from database import get_connection


file_path = "data/customer_data.csv"

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
    data[column] = pd.to_datetime(data[column], errors="coerce").dt.date

connection = get_connection()
cursor = connection.cursor()

columns = ", ".join(data.columns)
placeholders = ", ".join(["%s"] * len(data.columns))

query = f"""
    INSERT INTO customers ({columns})
    VALUES ({placeholders})
"""

for row in data.itertuples(index=False, name=None):
    cursor.execute(query, row)

connection.commit()

cursor.close()
connection.close()

print("Data loaded successfully")
print("Rows loaded:", len(data))