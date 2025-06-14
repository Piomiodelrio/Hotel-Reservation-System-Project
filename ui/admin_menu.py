from data_access.hotel_dao import HotelDAO
from data_access.booking_dao import BookingDAO
from data_access.room_dao import RoomDAO
from data_access.address_dao import AddressDAO
from data_access.room_type_dao import RoomTypeDAO
from data_access.facility_dao import FacilityDAO



class AdminMenu:
    def start(self):
        print("\n--- Admin Menu ---")
        while True:
            print("\n1. View All Hotels")
            print("2. View All Bookings")
            print("3. View Rooms & Features")
            print("4. Add a New Hotel")
            print("5. Update Existing Hotel")
            print("6. Manage Room Types")
            print("7. Manage Facilities")
            print("8. Delete Hotel")
            print("9. Exit")



            choice = input("Choose an option: ")

            if choice == '1':
                self.show_all_hotels()
            elif choice == '2':
                self.show_all_bookings()
            elif choice == '3':
                self.show_all_rooms()
            elif choice == '4':
                self.add_hotel()
            elif choice == '5':
                self.update_hotel()
            elif choice == '6':
                self.manage_room_types()
            elif choice == '7':
                self.manage_facilities()
            elif choice == '8':
                self.delete_hotel()
            elif choice == '9':
                break

            else:
                print("Invalid option.")


    def show_all_hotels(self):
        hotels = HotelDAO.get_all_hotels()
        for hotel in hotels:
            print(f"{hotel.hotel_id}: {hotel.name} ({hotel.stars} stars) - {hotel.address.city}")

    def show_all_bookings(self):
        bookings = BookingDAO.get_all_bookings()
        for b in bookings:
            print(f"Booking {b.booking_id} | Guest {b.guest.full_name} | Room {b.room.room_number} | {b.check_in} to {b.check_out} | Cancelled: {b.is_cancelled}")

    def show_all_rooms(self):
        rooms = RoomDAO.get_all_rooms()

        print("\n{:<35} {:<10} {:<20} {:<10} {:<12}".format("Hotel Name", "Room #", "Room Type", "Price", "Max Guests"))
        print("-" * 95)

        for room in rooms:
            print("{:<35} {:<10} {:<20} ${:<9.2f} {:<12}".format(
                room.hotel_name,
                room.room_number,
                room.room_type.description,
                room.price_per_night,
                room.room_type.max_guests
            ))



    def add_hotel(self):
        try:
            name = input("Enter hotel name: ")
            stars = int(input("Enter star rating: "))
            city = input("Enter city: ")
            street = input("Enter street: ")
            zip_code = input("Enter ZIP code: ")
            hotel = HotelDAO.insert_hotel(name, stars, city, street, zip_code)
            print(f"Hotel added successfully: {hotel.name} (ID: {hotel.hotel_id})")
        except Exception as e:
            print(f"Error adding hotel: {e}")

    def update_hotel(self):
        try:
            hotel_id = int(input("Enter hotel ID to update: "))
            name = input("New name: ")
            stars = int(input("New star rating: "))
            city = input("New city: ")
            street = input("New street: ")
            zip_code = input("New ZIP: ")

            address = AddressDAO.insert_address(city, street, zip_code)
            HotelDAO.update_hotel(hotel_id, name, stars, address.address_id)
            print("Hotel updated.")
        except Exception as e:
            print(f"Error updating hotel: {e}")

    def delete_hotel(self):
        try:
            hotel_id = int(input("Enter hotel ID to delete: "))
            confirm = input("Are you sure? (y/n): ")
            if confirm.lower() == 'y':
                HotelDAO.delete_hotel(hotel_id)
                print("Hotel deleted.")
        except Exception as e:
            print(f"Error deleting hotel: {e}")

    def manage_room_types(self):
        while True:
            print("\n--- Room Type Management ---")
            print("1. View Room Types")
            print("2. Add Room Type")
            print("3. Update Room Type")
            print("4. Delete Room Type")
            print("5. Back to Admin Menu")
            choice = input("Choose an option: ")

            if choice == '1':
                types = RoomTypeDAO.get_all_room_types()
                for t in types:
                    print(f"{t.type_id}: {t.description} (Max guests: {t.max_guests})")

            elif choice == '2':
                desc = input("Enter description: ")
                max_guests = int(input("Enter max guests: "))
                rt = RoomTypeDAO.insert_room_type(desc, max_guests)
                print(f"Room Type added: {rt.description}")

            elif choice == '3':
                type_id = int(input("Enter type ID to update: "))
                desc = input("New description: ")
                max_guests = int(input("New max guests: "))
                RoomTypeDAO.update_room_type(type_id, desc, max_guests)
                print("Room Type updated.")

            elif choice == '4':
                type_id = int(input("Enter type ID to delete: "))
                RoomTypeDAO.delete_room_type(type_id)
                print("Room Type deleted.")

            elif choice == '5':
                break

            else:
                print("Invalid option.")

    def manage_facilities(self):
        while True:
            print("\n--- Facility Management ---")
            print("1. View Facilities")
            print("2. Add Facility")
            print("3. Update Facility")
            print("4. Delete Facility")
            print("5. Back to Admin Menu")

            choice = input("Choose an option: ")

            if choice == '1':
                facilities = FacilityDAO.get_all_facilities()
                for f in facilities:
                    print(f"{f.facility_id}: {f.name}")

            elif choice == '2':
                name = input("Enter facility name: ")
                facility = FacilityDAO.insert_facility(name)
                print(f"Facility added: {facility.name} (ID: {facility.facility_id})")

            elif choice == '3':
                try:
                    facility_id = int(input("Enter facility ID to update: "))
                    new_name = input("Enter new name: ")
                    FacilityDAO.update_facility(facility_id, new_name)
                    print("Facility updated.")
                except Exception as e:
                    print(f"Error: {e}")

            elif choice == '4':
                try:
                    facility_id = int(input("Enter facility ID to delete: "))
                    FacilityDAO.delete_facility(facility_id)
                    print("Facility deleted.")
                except Exception as e:
                    print(f"Error: {e}")

            elif choice == '5':
                break
            else:
                print("Invalid option.")

