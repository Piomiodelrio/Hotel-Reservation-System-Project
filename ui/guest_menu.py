from business_logic.hotel_service import HotelService
from business_logic.availability_service import AvailabilityService
from business_logic.booking_service import BookingService
from data_access.room_dao import RoomDAO
from datetime import datetime
from model.guest import Guest
from data_access.guest_dao import GuestDAO
from data_access.guest_dao import GuestDAO
from data_access.address_dao import AddressDAO  # ← Make sure this import is present

class GuestMenu:
    def __init__(self):
        self.hotel_service = HotelService()

from data_access.guest_dao import GuestDAO  # <-- ADD THIS

class GuestMenu:
    def __init__(self):
        self.hotel_service = HotelService()

    def start(self):
        print("\n--- Guest Menu ---")
        guest = None

        while not guest:
            print("\n1. Login with Guest ID")
            print("2. Register as New Guest")
            print("3. Exit")
            choice = input("Choose an option: ")

            if choice == '1':
                try:
                    guest_id = int(input("Enter your Guest ID: "))
                    guest = GuestDAO.get_guest_by_id(guest_id)
                    if not guest:
                        print("Guest not found.")
                except Exception:
                    print("Invalid Guest ID.")

            elif choice == '2':
                full_name = input("Enter your full name: ")
                email = input("Enter email: ")

                # Split name into first and last name
                name_parts = full_name.strip().split()
                if len(name_parts) < 2:
                    print("Please enter both first and last name.")
                    continue
                first_name = name_parts[0]
                last_name = " ".join(name_parts[1:])

                # Prompt for address
                print("\n--- Address Details ---")
                street = input("Street: ")
                city = input("City: ")
                zip_code = input("Zip Code: ")

                # Insert address and get address_id
                address = AddressDAO.insert_address(street, city, zip_code)

                # Insert guest
                guest = GuestDAO.insert_guest(first_name, last_name, email, address.address_id)
                print(f"\nRegistered! Your Guest ID is {guest.guest_id}")


            elif choice == '3':
                return
            else:
                print("Invalid choice.")

        # After login/registration, show main menu
        self.main_menu(guest.guest_id)



    def search_flow(self, guest_id):
        city = input("Enter city name: ").strip()
        hotels = self.hotel_service.search_hotels_by_city(city)

        if not hotels:
            print("No hotels found.")
            return

        print("\nAvailable Hotels:")
        for hotel in hotels:
            print(f"{hotel.hotel_id}: {hotel.name} ({hotel.stars} stars)")

        hotel_id = int(input("Enter Hotel ID to see rooms: "))
        rooms = self.hotel_service.get_rooms_for_hotel(hotel_id)

        try:
            guests = int(input("Enter number of guests: "))
            rooms = [r for r in rooms if r.max_guests >= guests]

            star_filter = input("Filter by star rating? (y/n): ").strip().lower()
            if star_filter == 'y':
                stars = int(input("Enter star rating: "))
                hotels = self.hotel_service.filter_hotels_by_star(hotels, stars)

            date_filter = input("Check room availability? (y/n): ").strip().lower()
            if date_filter == 'y':
                check_in = datetime.strptime(input("Check-in (YYYY-MM-DD): "), "%Y-%m-%d")
                check_out = datetime.strptime(input("Check-out (YYYY-MM-DD): "), "%Y-%m-%d")
                rooms = AvailabilityService.filter_available_rooms(rooms, check_in, check_out)
            else:
                check_in = check_out = None

            if not rooms:
                print("No rooms match your criteria.")
                return

            print("\nAvailable Rooms:")
            for room in rooms:
                print(f"Room {room.room_number} | {room.room_type.description} | Max guests: {room.max_guests} | ${room.price_per_night:.2f}/night")


            if date_filter == 'y':
                book = input("Would you like to book a room? (y/n): ").strip().lower()
                if book == 'y':
                    room_num = input("Enter room number to book: ")
                    room = next((r for r in rooms if r.room_number == room_num), None)
                    if room:
                        booking = BookingService.create_booking(guest_id, room, check_in, check_out)
                        print(f"Booking successful. Booking ID: {booking.booking_id}, Total: ${booking.total_amount:.2f}")
                    else:
                        print("Room not found.")
        except Exception as e:
            print(f"Error: {e}")

    def main_menu(self, guest_id):
        while True:
            print("\n1. Search Hotels by City")
            print("2. View My Bookings")
            print("3. Exit")
            choice = input("Choose an option: ")

            if choice == '1':
                self.search_flow(guest_id)
            elif choice == '2':
                self.view_guest_bookings(guest_id)
            elif choice == '3':
                break
            else:
                print("Invalid choice.")

    def view_guest_bookings(self, guest_id):
        bookings = BookingService.get_bookings_by_guest(guest_id)  
        if not bookings:
            print("You have no bookings.")
            return

        for b in bookings:
            status = "Cancelled" if b.is_cancelled else "Confirmed"
            print(f"Booking #{b.booking_id} | Room {b.room.room_number} | {b.check_in} to {b.check_out} | Status: {status}")



