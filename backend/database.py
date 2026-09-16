import psycopg2


def get_connection():
    connection = psycopg2.connect(
        host="localhost",
        database="smart_customer_db",
        user="postgres",
        password="YOUR_POSTGRES_PASSWORD",
        port=5432
    )

    return connection


if __name__ == "__main__":
    connection = get_connection()

    print("PostgreSQL connection successful")

    connection.close()