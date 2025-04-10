import tkinter as tk

class Ausgabe:
    def __init__(self, betrag, kategorie):
        self.betrag = betrag
        self.kategorie = kategorie

    def __str__(self):
        return f"{self.kategorie}: {self.betrag} EUR"

def speichern():
    betrag = entry_betrag.get()
    kategorie = entry_kategorie.get()
    ausgabe = Ausgabe(betrag, kategorie)
    
    with open("ausgaben.txt", "a") as f:
        f.write(str(ausgabe) + "\n")
    
    entry_betrag.delete(0, tk.END)
    entry_kategorie.delete(0, tk.END)

fenster = tk.Tk()
fenster.title("Haushaltsbuch")

label_betrag = tk.Label(fenster, text="Betrag:")
label_betrag.pack()
entry_betrag = tk.Entry(fenster)
entry_betrag.pack()

label_kategorie = tk.Label(fenster, text="Kategorie:")
label_kategorie.pack()
entry_kategorie = tk.Entry(fenster)
entry_kategorie.pack()

button_speichern = tk.Button(fenster, text="Speichern", command=speichern)
button_speichern.pack()

fenster.mainloop()
