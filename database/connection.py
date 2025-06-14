import sqlite3

class DBConnection:
    _connection = None

    @staticmethod
    def get_connection():
        if DBConnection._connection is None:
            DBConnection._connection = sqlite3.connect("database/hotel_reservation_sample.db")
            DBConnection._connection.row_factory = sqlite3.Row
        return DBConnection._connection

    @staticmethod
    def close_connection():
        if DBConnection._connection:
            DBConnection._connection.close()
            DBConnection._connection = None
