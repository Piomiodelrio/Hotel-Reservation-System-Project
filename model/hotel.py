from model.address import Address

class Hotel:
    def __init__(self, hotel_id, name, stars, address: Address):
        self.hotel_id = hotel_id
        self.name = name
        self.stars = stars
        self.address = address
        self.rooms = []

    def __str__(self):
        return f"{self.name} ({self.stars}★), Address: {self.address}"
