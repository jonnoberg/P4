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

    # Functie om de score toe te voegen aan de database
    def add_score(self, naam, score):
        print("Add score: " + naam + ", " + str(score))
        connection = sqlite3.connect('lingo.sqlite3')
        cursor = connection.cursor()
        query = "INSERT INTO highscores (name, score) VALUES(?, ?)"
        cursor.execute(query, (naam, score))
        connection.commit()
        connection.close()
