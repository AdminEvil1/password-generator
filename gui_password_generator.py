import tkinter as tk
import string
import random

fenster = tk.Tk()
fenster.title("Passwort-Generator")
fenster.geometry("300x200")

# Textfeld zur Anzeige des Passworts
output_label = tk.Label(fenster, text="Hier erscheint dein Passwort")
output_label.pack(pady=10)

sonderzeichen_var = tk.BooleanVar()
sonderzeichen_check = tk.Checkbutton(fenster, text="Sonderzeichen benutzen", variable=sonderzeichen_var)
sonderzeichen_check.pack()


# Funktion zum Generieren
laenge_label = tk.Label(fenster, text="Passwortlänge (4–24):")
laenge_label.pack()

laenge_eingabe = tk.Entry(fenster)
laenge_eingabe.pack()

def generate_password():
    zeichen = string.ascii_letters + string.digits
    if sonderzeichen_var.get():
        zeichen += string.punctuation

    try:
        laenge = int(laenge_eingabe.get())
        if not 4 <= laenge <= 24:
            output_label.config(text="❗ Länge muss 4–24 sein")
            return
    except ValueError:
        output_label.config(text="❗ Bitte Zahl eingeben")
        return

    pw = ''.join(random.choices(zeichen, k=laenge))
    output_label.config(text=pw)

def copy_to_clipboard():
    passwort = output_label.cget("text")
    fenster.clipboard_clear()
    fenster.clipboard_append(passwort)
    fenster.update()


# Button
button = tk.Button(fenster, text="Passwort generieren", command=generate_password)
button.pack(pady=10)

copy_button = tk.Button(fenster, text="Passwort kopieren", command=copy_to_clipboard)
copy_button.pack(pady=5)



fenster.mainloop()
