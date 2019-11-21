import sqlite3


class ContextManagerSQlite:

    def __init__(self, db_name):
        self._db_file = sqlite3.connect(db_name)

    def __enter__(self):
        return self._db_file.cursor()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._db_file.commit()
        self._db_file.close()