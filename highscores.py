import sqlite3

class Highscores:

    def __init__(self):
        # controleer of de tabel bestaat en eventueel aanmaken
        self.create_table()
    
    def create_table(self):
        connection = sqlite3.connect('lingo.sqlite3')
        cursor = connection.cursor()
        cursor.execute("""CREATE TABLE IF NOT EXISTS highscores (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            score INTEGER NOT NULL
            );""")
        connection.close()
