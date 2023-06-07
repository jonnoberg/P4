class Lingo:

    # Constructor met de declaratie van het atribuut woord.
    def __init__(self):
        self.woord = str.lower("Lingo")
        self.beurt = 1

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