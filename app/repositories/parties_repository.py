import sqlite3


class PartiesRepository:

    def __init__(self, db_path):
        self.db_path = db_path

    def get_parties(self):
        connexion = sqlite3.connect(self.db_path)
        connexion.row_factory = sqlite3.Row

        cursor = connexion.execute("""
            SELECT *
            FROM parties
        """)

        parties = cursor.fetchall()

        connexion.close()

        return parties