from model.room_type import RoomType
from model.facility import Facility

class Room:
    def __init__(self, room_id, room_number, hotel_id, room_type: RoomType, price_per_night, hotel_name=None):
        self.room_id = room_id
        self.room_number = room_number
        self.hotel_id = hotel_id
        self.room_type = room_type
        self.price_per_night = price_per_night
        self.facilities = []
        self.hotel_name = hotel_name  # new line

    @property
    def max_guests(self):
        return self.room_type.max_guests

    def __str__(self):
        facilities_str = ", ".join([str(f) for f in self.facilities])
        hotel_info = f" | Hotel: {self.hotel_name}" if self.hotel_name else ""
        return f"Room {self.room_number} ({self.room_type.description}) - ${self.price_per_night:.2f}/night{hotel_info}\n  Facilities: {facilities_str}"

