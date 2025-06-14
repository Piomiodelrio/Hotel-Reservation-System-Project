import sqlite3

class DatabaseConnection:
    _connection = None

    @staticmethod
    def get_connection(db_path='database/hotel_reservation_sample.db'):
        if DatabaseConnection._connection is None:
            DatabaseConnection._connection = sqlite3.connect(db_path)
            DatabaseConnection._connection.row_factory = sqlite3.Row  # Enables dict-like access
        return DatabaseConnection._connection
