from data_access.database_connection import DatabaseConnection
from model.booking import Booking
from model.invoice import Invoice
from data_access.guest_dao import GuestDAO
from data_access.room_dao import RoomDAO
from model.room import Room
from model.booking import Booking


class BookingDAO:
    @staticmethod
    def get_all_bookings():
        conn = DatabaseConnection.get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Booking ORDER BY check_in_date")
        bookings = []
        for row in cursor.fetchall():
            guest = GuestDAO.get_guest_by_id(row["guest_id"])  # ✅ Fetch full Guest
            room = RoomDAO.get_room_by_id(row["room_id"])      # ✅ Fetch full Room

            bookings.append(Booking(
                booking_id=row["booking_id"],
                guest=guest,
                room=room,
                check_in=row["check_in_date"],
                check_out=row["check_out_date"],
                is_cancelled=bool(row["is_cancelled"]),
                total_amount=row["total_amount"]
            ))
        return bookings


    @staticmethod
    def insert_booking(booking: Booking):
        conn = DatabaseConnection.get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO Booking (guest_id, room_id, check_in_date, check_out_date, is_cancelled, total_amount)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (
            booking.guest.guest_id,
            booking.room.room_id,
            booking.check_in_date,
            booking.check_out_date,
            int(booking.is_cancelled),
            booking.total_amount
        ))
        conn.commit()
        booking.booking_id = cursor.lastrowid
        return booking

    @staticmethod
    def cancel_booking(booking_id: int):
        conn = DatabaseConnection.get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            UPDATE Booking SET is_cancelled = 1 WHERE booking_id = ?
        """, (booking_id,))
        conn.commit()

    @staticmethod
    def get_bookings_for_room(room_id: int):
        conn = DatabaseConnection.get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT * FROM Booking
            WHERE room_id = ? AND is_cancelled = 0
        """, (room_id,))
        bookings = []
        for row in cursor.fetchall():
            guest = GuestDAO.get_guest_by_id(row["guest_id"])
            room = RoomDAO.get_room_by_id(row["room_id"])
            bookings.append(Booking(
                booking_id=row["booking_id"],
                guest=guest,
                room=room,
                check_in=row["check_in_date"],
                check_out=row["check_out_date"],
                is_cancelled=bool(row["is_cancelled"]),
                total_amount=row["total_amount"]
            ))

        return bookings

    @staticmethod
    def get_invoice_for_booking(booking_id: int):
        conn = DatabaseConnection.get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT * FROM Invoice WHERE booking_id = ?
        """, (booking_id,))
        row = cursor.fetchone()
        if row:
            return Invoice(
                invoice_id=row["invoice_id"],
                booking_id=row["booking_id"],
                issue_date=row["issue_date"],
                total_amount=row["total_amount"]
            )
        return None

    @staticmethod
    def create_invoice(booking: Booking):
        conn = DatabaseConnection.get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO Invoice (booking_id, total_amount)
            VALUES (?, ?)
        """, (booking.booking_id, booking.total_amount))
        conn.commit()
        return BookingDAO.get_invoice_for_booking(booking.booking_id)
    
    @staticmethod
    def get_bookings_by_guest(guest_id):
        conn = DatabaseConnection.get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT b.*, 
                r.room_number, r.hotel_id, r.price_per_night, 
                rt.description AS room_type
            FROM Booking b
            JOIN Room r ON b.room_id = r.room_id
            JOIN Room_Type rt ON r.type_id = rt.type_id
            WHERE b.guest_id = ?
        """, (guest_id,))
        
        bookings = []
        for row in cursor.fetchall():
            room = Room(
                room_id=row["room_id"],
                room_number=row["room_number"],
                hotel_id=row["hotel_id"],
                room_type=row["room_type"],  # ← from Room_Type.description
                price_per_night=row["price_per_night"]
            )
            guest = GuestDAO.get_guest_by_id(row["guest_id"])
            booking = Booking(
                booking_id=row["booking_id"],
                guest=guest,
                room=room,
                check_in=row["check_in_date"],
                check_out=row["check_out_date"],
                total_amount=row["total_amount"],
                is_cancelled=bool(row["is_cancelled"])
            )
            bookings.append(booking)
        return bookings
