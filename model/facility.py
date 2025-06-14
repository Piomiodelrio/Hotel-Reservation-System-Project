class Facility:
    def __init__(self, facility_id, name):
        self.facility_id = facility_id
        self.name = name

    def __str__(self):
        return self.name
