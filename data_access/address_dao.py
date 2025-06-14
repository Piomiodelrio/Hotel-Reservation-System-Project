from model.address import Address
from data_access.database_connection import DatabaseConnection

class AddressDAO:
    @staticmethod
    def get_address_by_id(address_id):
        conn = DatabaseConnection.get_connection()
        if conn is None:
            raise Exception("Database connection is closed or unavailable.")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Address WHERE address_id = ?", (address_id,))
        row = cursor.fetchone()
        if row:
            return Address(row["address_id"], row["street"], row["city"], row["zip_code"])
        return None

    @staticmethod
    def insert_address(city, street, zip_code):
        conn = DatabaseConnection.get_connection()
        if conn is None:
            raise Exception("Database connection is closed or unavailable.")
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO Address (street, city, zip_code)
            VALUES (?, ?, ?)
        """, (street, city, zip_code))
        conn.commit()
        address_id = cursor.lastrowid
        return Address(address_id, street, city, zip_code)
