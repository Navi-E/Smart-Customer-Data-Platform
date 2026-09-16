from flask import Flask, jsonify
from flask_cors import CORS
from database import get_connection

app = Flask(__name__)
CORS(app)


@app.route("/")
def home():
    return jsonify({
        "message": "Smart Customer Data Platform API is running"
    })


@app.route("/api/customers")
def get_customers():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM customers LIMIT 100")
    rows = cursor.fetchall()

    columns = [desc[0] for desc in cursor.description]

    customers = []

    for row in rows:
        customer = dict(zip(columns, row))
        customers.append(customer)

@app.route("/api/stats")
def get_stats():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("SELECT COUNT(*) FROM customers")
    total_customers = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM customers WHERE anomaly = -1")
    anomalies = cursor.fetchone()[0]

    cursor.execute("SELECT AVG(account_balance) FROM customers")
    average_balance = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM customers WHERE loan_status = 'Approved'")
    approved_loans = cursor.fetchone()[0]

    cursor.close()
    connection.close()

    return jsonify({
        "total_customers": total_customers,
        "anomalies": anomalies,
        "average_balance": round(float(average_balance), 2),
        "approved_loans": approved_loans
    })

    cursor.close()
    connection.close()

    return jsonify(customers)


if __name__ == "__main__":
    app.run(debug=True)