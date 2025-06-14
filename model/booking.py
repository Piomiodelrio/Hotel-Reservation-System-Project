from model.guest import Guest
from model.room import Room

class Booking:
    def __init__(self, booking_id, guest: Guest, room: Room, check_in, check_out, is_cancelled, total_amount):
        self.booking_id = booking_id
        self.guest = guest
        self.room = room
        self.check_in = check_in
        self.check_out = check_out
        self.is_cancelled = is_cancelled
        self.total_amount = total_amount

    def __str__(self):
        status = "Cancelled" if self.is_cancelled else "Confirmed"
        return f"Booking #{self.booking_id}: {self.guest.full_name} → Room {self.room.room_number} from {self.check_in} to {self.check_out} | Status: {status}"
