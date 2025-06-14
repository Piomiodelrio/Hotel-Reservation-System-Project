from ui.guest_menu import GuestMenu
from ui.admin_menu import AdminMenu

def main():
    while True:
        print("\n--- Welcome to the Hotel Reservation System ---")
        print("1. Guest")
        print("2. Admin")
        print("3. Exit")

        choice = input("Choose your role: ")

        if choice == '1':
            GuestMenu().start()
        elif choice == '2':
            AdminMenu().start()
        elif choice == '3':
            print("Thank you for using the system. Goodbye!")
            break
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()
