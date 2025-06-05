import string
import random

while True:
    try:
        laenge = int(input("Wie lange soll das Passwort sein?"))
        if 0 < laenge <= 12:
            print("Das Passwort ist mit einer Länge von " + str(laenge) + " in ordnung!")
            break
        else:
            print("Das ist leider nicht möglich! Maximal 12 Zeichen!")
    except ValueError:
        print("Bitte gib eine gültige Zahl ein!")
    


zeichen = string.ascii_letters + string.digits
special_zeichen = zeichen + string.punctuation
while True:
    try:

        sonderzeichen = input("Darf das Zeichen Sonderzeichen haben?").lower()
        if sonderzeichen == "ja": 
            print("Super!")
            zeichenliste = special_zeichen
            
            break
        else:
            print("Keine sonderzeichen!")
            zeichenliste = zeichen
            break
            
    except ValueError:
        print("Bitte gib eine gültige Antwort ein!")

while True:
    try:
        anzahl = int(input("Wieviele Passwörter möchtest du generiert haben?"))
        if 0 < anzahl <= 10:
            print(f"Du bekommst {anzahl} verschiedene Passwörter")
            break
    except ValueError:
        print("Das ist leider nicht möglich. Versuche es erneut!")

for i in range(anzahl):
    passwort =  ''.join(random.choices(zeichenliste, k=laenge))
    print(f"{i+1}. {passwort}")