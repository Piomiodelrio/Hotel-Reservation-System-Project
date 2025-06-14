from model.guest import Guest
from data_access.address_dao import AddressDAO
from data_access.database_connection import DatabaseConnection
from model.address import Address
from model.guest import Guest

class GuestDAO:
    @staticmethod
    def get_guest_by_email(email):
        conn = DatabaseConnection.get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Guest WHERE email = ?", (email,))
        row = cursor.fetchone()
        if row:
            address = AddressDAO.get_address_by_id(row["address_id"])
            return Guest(row["guest_id"], row["first_name"], row["last_name"], row["email"], address)
        return None

    @staticmethod
    def get_guest_by_id(guest_id):
        conn = DatabaseConnection.get_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM Guest g JOIN Address a ON g.address_id = a.address_id WHERE g.guest_id = ?", (guest_id,))
        row = cursor.fetchone()
        if row:
            address = Address(row["address_id"], row["street"], row["city"], row["zip_code"])
            guest = Guest(
                guest_id=row["guest_id"],
                first_name=row["first_name"],
                last_name=row["last_name"],
                email=row["email"],
                address=address
            )
            return guest
        return None

    @staticmethod
    def insert_guest(first_name, last_name, email, address_id):
        existing_guest = GuestDAO.get_guest_by_email(email)
        if existing_guest:
            print("Guest with this email already exists. Logging you in instead.")
            return existing_guest

        conn = DatabaseConnection.get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO Guest (first_name, last_name, email, address_id)
            VALUES (?, ?, ?, ?)
        """, (first_name, last_name, email, address_id))
        conn.commit()
        guest_id = cursor.lastrowid
        address = AddressDAO.get_address_by_id(address_id)
        return Guest(guest_id, first_name, last_name, email, address)


