from highscores import Highscores
import sqlite3

# test het maken van de tabel
scores = Highscores()

# test het toevoegen van een score
scores.add_score("Laura", 100)