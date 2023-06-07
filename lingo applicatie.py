import random
import tkinter as tk

class Lingo:
    def __init__(self, woordenlijst):
        self.woordenlijst = woordenlijst
        self.te_raden_woord = ""
        self.pogingen = 0
        
        self.window = tk.Tk()
        self.window.title("Lingo")
        
        self.label = tk.Label(self.window, text="Lingo gestart!")
        self.label.pack()
        
        self.woord_entry = tk.Entry(self.window)
        self.woord_entry.pack()
        
        self.raad_button = tk.Button(self.window, text="Raad", command=self.raad_woord)
        self.raad_button.pack()
    
    def start(self):
        self.te_raden_woord = random.choice(self.woordenlijst)
        self.pogingen = 0
        self.label.config(text="Probeer het woord te raden:")
    
    def raad_woord(self):
        woord = self.woord_entry.get()
        
        if len(woord) != len(self.te_raden_woord):
            self.label.config(text="Het woord moet {} letters lang zijn.".format(len(self.te_raden_woord)))
            return
        
        self.pogingen += 1
        if woord == self.te_raden_woord:
            self.label.config(text="Gefeliciteerd, je hebt het woord geraden in {} poging(en)!".format(self.pogingen))
            self.raad_button.config(state=tk.DISABLED)
        else:
            feedback = ""
            for i in range(len(woord)):
                if woord[i] == self.te_raden_woord[i]:
                    feedback += woord[i]
                elif woord[i] in self.te_raden_woord:
                    feedback += "?"
                else:
                    feedback += "*"
            
            if self.pogingen >= 5:
                self.label.config(text="Helaas, je hebt het woord niet geraden. Het woord was {}.".format(self.te_raden_woord))
                self.raad_button.config(state=tk.DISABLED)
            else:
                self.label.config(text="Niet correct. Feedback: {}. Poging: {}/5".format(feedback, self.pogingen))
        
        self.woord_entry.delete(0, tk.END)

# Voorbeeldgebruik:
woordenlijst = ["appel", "tafel", "stoel", "fiets", "stoep", "brood", "kaart", "water", "taart", "stoer", "wagen", "schoen", "molen", "koken", "spoor", "piano", "vrouw", "kabel", "kleur", "vogel", "bloem", "lunch", "ruzie", "grond", "hobby", "steen", "pauze", "droom", "zeven", "bocht", "krant", "schat", "horen", "toren", "dagen"]
lingo = Lingo(woordenlijst)
lingo.start()

lingo.window.mainloop()
