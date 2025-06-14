class Address:
    def __init__(self, address_id, street, city, zip_code):
        self.address_id = address_id
        self.street = street
        self.city = city
        self.zip_code = zip_code

    def __str__(self):
        return f"{self.street}, {self.city}, {self.zip_code}"
