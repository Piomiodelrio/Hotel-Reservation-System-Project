from model.hotel import Hotel
from data_access.address_dao import AddressDAO
from data_access.database_connection import DatabaseConnection

class HotelDAO:
    @staticmethod
    def get_hotels_by_city(city):
        conn = DatabaseConnection.get_connection()
        cursor = conn.cursor()
        query = """SELECT * FROM Hotel h 
                   JOIN Address a ON h.address_id = a.address_id 
                   WHERE a.city = ?"""
        cursor.execute(query, (city,))
        hotels = []
        for row in cursor.fetchall():
            address = AddressDAO.get_address_by_id(row["address_id"])
            hotel = Hotel(row["hotel_id"], row["name"], row["stars"], address)
            hotels.append(hotel)
        return hotels

    @staticmethod
    def get_hotel_by_id(hotel_id):
        conn = DatabaseConnection.get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Hotel WHERE hotel_id = ?", (hotel_id,))
        row = cursor.fetchone()
        if row:
            address = AddressDAO.get_address_by_id(row["address_id"])
            return Hotel(row["hotel_id"], row["name"], row["stars"], address)
        return None
    
    @staticmethod
    def update_hotel(hotel_id, name, stars, address_id):
        conn = DatabaseConnection.get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            UPDATE Hotel SET name = ?, stars = ?, address_id = ?
            WHERE hotel_id = ?
        """, (name, stars, address_id, hotel_id))
        conn.commit()

    @staticmethod
    def delete_hotel(hotel_id):
        conn = DatabaseConnection.get_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM Hotel WHERE hotel_id = ?", (hotel_id,))
        conn.commit()

    @staticmethod
    def get_all_hotels():
        conn = DatabaseConnection.get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT h.*, a.city, a.street, a.zip_code
            FROM Hotel h
            JOIN Address a ON h.address_id = a.address_id
        """)
        hotels = []
        for row in cursor.fetchall():
            address = AddressDAO.get_address_by_id(row['address_id'])
            hotels.append(Hotel(row['hotel_id'], row['name'], row['stars'], address))
        return hotels
    
    @staticmethod
    def insert_hotel(name, stars, city, street, zip_code):
        address = AddressDAO.insert_address(city, street, zip_code)
        conn = DatabaseConnection.get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO Hotel (name, stars, address_id) VALUES (?, ?, ?)",
            (name, stars, address.address_id)
        )
        conn.commit()
        hotel_id = cursor.lastrowid
        return Hotel(hotel_id, name, stars, address)



