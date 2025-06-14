class RoomType:
    def __init__(self, type_id, description, max_guests):
        self.type_id = type_id
        self.description = description
        self.max_guests = max_guests

    def __str__(self):
        return f"{self.description} (Max Guests: {self.max_guests})"
