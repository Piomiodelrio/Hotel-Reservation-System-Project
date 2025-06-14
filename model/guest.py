from model.user import User
from model.address import Address

class Guest(User):
    def __init__(self, guest_id, first_name, last_name, email, address: Address):
        full_name = f"{first_name} {last_name}"
        super().__init__(guest_id, full_name)
        self.first_name = first_name
        self.last_name = last_name
        self.guest_id = guest_id
        self.email = email
        self.address = address

    def __str__(self):
        return f"{self.full_name} <{self.email}>"
