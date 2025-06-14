from model.facility import Facility
from data_access.database_connection import DatabaseConnection

class FacilityDAO:
    @staticmethod
    def get_all_facilities():
        conn = DatabaseConnection.get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Facilities")
        return [Facility(row["facility_id"], row["facility_name"]) for row in cursor.fetchall()]

    @staticmethod
    def get_facilities_for_room(room_id):
        conn = DatabaseConnection.get_connection()
        cursor = conn.cursor()
        query = """
            SELECT f.facility_id, f.facility_name 
            FROM Facilities f
            JOIN Room_Facilities rf ON f.facility_id = rf.facility_id
            WHERE rf.room_id = ?
        """
        cursor.execute(query, (room_id,))
        return [Facility(row["facility_id"], row["facility_name"]) for row in cursor.fetchall()]

    @staticmethod
    def insert_facility(facility_name):
        conn = DatabaseConnection.get_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO Facilities (facility_name) VALUES (?)", (facility_name,))
        conn.commit()
        facility_id = cursor.lastrowid
        return Facility(facility_id, facility_name)

    @staticmethod
    def update_facility(facility_id, new_name):
        conn = DatabaseConnection.get_connection()
        cursor = conn.cursor()
        cursor.execute("UPDATE Facilities SET facility_name = ? WHERE facility_id = ?", (new_name, facility_id))
        conn.commit()

    @staticmethod
    def delete_facility(facility_id):
        conn = DatabaseConnection.get_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM Facilities WHERE facility_id = ?", (facility_id,))
        conn.commit()
