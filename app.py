import os
import time
import psycopg2

DB_HOST = os.getenv("DB_HOST", "my-postgres")
DB_NAME = os.getenv("DB_NAME", "mydb")
DB_USER = os.getenv("DB_USER", "user")
DB_PASS = os.getenv("DB_PASS", "pass")
DB_PORT = int(os.getenv("DB_PORT", "5432"))

def wait_for_postgres(retries=30, delay=1):
    for i in range(retries):
        try:
            conn = psycopg2.connect(
                host=DB_HOST, database=DB_NAME, user=DB_USER, password=DB_PASS, port=DB_PORT, connect_timeout=3
            )
            conn.close()
            print("Postgres is ready.")
            return True
        except Exception as e:
            print(f"Waiting for Postgres (attempt {i+1}/{retries}): {e}")
            time.sleep(delay)
    return False

def main():
    if not wait_for_postgres():
        print("Failed to connect to Postgres. Exiting.")
        return

    # 🔹 Ask user for input manually
    user_message = input("Enter a message to store in the database: ")

    conn = psycopg2.connect(
        host=DB_HOST, database=DB_NAME, user=DB_USER, password=DB_PASS, port=DB_PORT
    )
    try:
        with conn:
            with conn.cursor() as cur:
                cur.execute("""
                    CREATE TABLE IF NOT EXISTS items (
                        id SERIAL PRIMARY KEY,
                        message TEXT NOT NULL,
                        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                    );
                """)

                # Insert user message
                cur.execute("INSERT INTO items (message) VALUES (%s) RETURNING id;", (user_message,))
                inserted_id = cur.fetchone()[0]
                print(f"Inserted row id: {inserted_id}")

                # Read back the row
                cur.execute("SELECT * FROM items WHERE id = %s;", (inserted_id,))
                row = cur.fetchone()
                print("Stored data:", row)
    finally:
        conn.close()

if __name__ == "__main__":
    main()