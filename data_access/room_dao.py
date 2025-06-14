from model.room import Room
from data_access.room_type_dao import RoomTypeDAO
from data_access.facility_dao import FacilityDAO
from data_access.database_connection import DatabaseConnection
from model.room_type import RoomType
from model.facility import Facility

class RoomDAO:
    @staticmethod
    def get_rooms_by_hotel(hotel_id):
        conn = DatabaseConnection.get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT 
                Room.room_id,
                Room.room_number,
                Room.hotel_id,
                Room.type_id,
                Room.price_per_night,
                Room_Type.description,
                Room_Type.max_guests
            FROM Room
            JOIN Room_Type ON Room.type_id = Room_Type.type_id
            WHERE Room.hotel_id = ?
        """, (hotel_id,))
        
        rooms = []
        for row in cursor.fetchall():
            room_type = RoomType(
                type_id=row["type_id"],
                description=row["description"],
                max_guests=row["max_guests"]
            )
            room = Room(
                room_id=row["room_id"],
                room_number=row["room_number"],
                hotel_id=row["hotel_id"],
                room_type=room_type,
                price_per_night=row["price_per_night"]
            )
            room.facilities = FacilityDAO.get_facilities_for_room(room.room_id)
            rooms.append(room)
        return rooms

    
    @staticmethod
    def get_room_by_id(room_id: int):
        conn = DatabaseConnection.get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT 
                Room.room_id,
                Room.room_number,
                Room.hotel_id,
                Room.type_id,
                Room.price_per_night,
                Room_Type.description,
                Room_Type.max_guests
            FROM Room
            JOIN Room_Type ON Room.type_id = Room_Type.type_id
            WHERE Room.room_id = ?
        """, (room_id,))
        row = cursor.fetchone()

        if row:
            room_type = RoomType(
                type_id=row["type_id"],
                description=row["description"],
                max_guests=row["max_guests"]
            )
            room = Room(
                room_id=row["room_id"],
                room_number=row["room_number"],
                hotel_id=row["hotel_id"],
                room_type=room_type,
                price_per_night=row["price_per_night"]
            )
            return room
        return None
    
    @staticmethod
    def get_all_rooms():
        from database.connection import DBConnection
        from model.room import Room, RoomType

        conn = DBConnection.get_connection()
        cursor = conn.cursor()

        query = """
        SELECT 
            r.room_id, r.room_number, r.price_per_night,
            rt.type_id, rt.description, rt.max_guests,
            h.hotel_id, h.name
        FROM Room r
        JOIN Room_Type rt ON r.type_id = rt.type_id
        JOIN Hotel h ON r.hotel_id = h.hotel_id
        """
        cursor.execute(query)
        rows = cursor.fetchall()

        rooms = []
        for row in rows:
            room_type = RoomType(type_id=row[3], description=row[4], max_guests=row[5])
            room = Room(room_id=row[0], room_number=row[1], price_per_night=row[2],
                        room_type=room_type, hotel_id=row[6], hotel_name=row[7])
            rooms.append(room)

        return rooms

