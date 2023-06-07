import sqlite3
class Lingo:

    # Constructor met de declaratie van het atribuut woord.
    def __init__(self):
        self.woord = self.set_woord()
        self.beurt = 1

    # Functie om een woord te selecteren uit de database
    def set_woord(self):
        connection = sqlite3.connect('lingo.sqlite3')
        cursor = connection.execute('SELECT * FROM vijfletters ORDER BY RANDOM() LIMIT 1;')
        for row in cursor:
            woord = row[0]
        connection.close() 
        print(woord)
        return woord

    def validate_input(self, invoer):

        # Verhoog de beurt
        self.beurt += 1

        # Converteer de invoer string naar kleine letters
        invoer = str.lower(invoer)
        
        # Controleer of de invoer string gelijk is aan het te raden woord
        if (invoer == self.woord):
            return "gewonnen"
        
        # Controleer of het woord 5 letters heeft
        if ( len(invoer) != 5):
            return "Voer een woord in van 5 letters!"
        
        # vergelijk elke letter van de invoerstring met het te raden woord
        uitvoer = ""
        for i in range(5):
            if(invoer[i] == self.woord[i]):
                uitvoer += str.upper(invoer[i])
            elif(invoer[i] in self.woord):
                uitvoer += str.upper(invoer[i])
            else:
                uitvoer += "_" 
        return uitvoer

        # Geef de uitvoer van de string terug
        return "OK"