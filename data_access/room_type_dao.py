from model.room_type import RoomType
from data_access.database_connection import DatabaseConnection

class RoomTypeDAO:
    @staticmethod
    def get_room_type_by_id(type_id):
        conn = DatabaseConnection.get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Room_Type WHERE type_id = ?", (type_id,))
        row = cursor.fetchone()
        if row:
            return RoomType(row["type_id"], row["description"], row["max_guests"])
        return None
    
    @staticmethod
    def get_all_room_types():
        conn = DatabaseConnection.get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Room_Type")
        rows = cursor.fetchall()
        return [RoomType(row["type_id"], row["description"], row["max_guests"]) for row in rows]

    @staticmethod
    def insert_room_type(description, max_guests):
        conn = DatabaseConnection.get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO Room_Type (description, max_guests)
            VALUES (?, ?)
        """, (description, max_guests))
        conn.commit()
        type_id = cursor.lastrowid
        return RoomType(type_id, description, max_guests)

    @staticmethod
    def update_room_type(type_id, description, max_guests):
        conn = DatabaseConnection.get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            UPDATE Room_Type
            SET description = ?, max_guests = ?
            WHERE type_id = ?
        """, (description, max_guests, type_id))
        conn.commit()

    @staticmethod
    def delete_room_type(type_id):
        conn = DatabaseConnection.get_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM Room_Type WHERE type_id = ?", (type_id,))
        conn.commit()
