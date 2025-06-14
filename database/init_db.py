import sqlite3

def initialize_database():
    with open("Hotel Reservation Sql script.txt", "r", encoding="utf-8") as file:
        sql_script = file.read()

    conn = sqlite3.connect("hotel_reservation_sample.db")
    cursor = conn.cursor()

    try:
        cursor.executescript(sql_script)
        conn.commit()
        print("Database initialized successfully.")
    except sqlite3.Error as e:
        print("Database initialization failed:", e)
    finally:
        conn.close()

if __name__ == "__main__":
    initialize_database()
