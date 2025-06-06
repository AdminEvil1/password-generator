# 🔐 Passwort-Generator (Python)

Ein einfacher, interaktiver Passwortgenerator mit grafischer Benutzeroberfläche (GUI).  
Du kannst selbst bestimmen:

- die **Länge** (4-24 Zeichen)
- ob **Sonderzeichen** enthalten sein sollen
- das generierte Passwort per Klick kopieren

---

## 🚀 So funktioniert es

1. Du gibst eine gewünschte Länge ein

2. Entscheidest, ob Sonderzeichen wie !@#$ erlaubt sind

3. Klickst auf „Passwort generieren“

4. Das Passwort erscheint direkt im Fenster

5. Mit „Passwort kopieren“ landet es direkt in deiner Zwischenablage

⚠️ Hinweis für Windows/AVG-Nutzer

Die `.exe`-Datei wurde mit PyInstaller erstellt und ist sicher.  
Einige Antivirenprogramme (z. B. AVG oder Windows Defender) könnten sie fälschlich als Bedrohung einstufen (False Positive).

Wenn das passiert:

1. Öffne dein Antivirenprogramm (z. B. AVG)
2. Gehe zu Quarantäne
3. Stelle die Datei wieder her und füge sie zur Ausnahme hinzu

✅ Du kannst den Code hier auf GitHub einsehen – alles ist Open Source.

---

## 🧩 Chrome-Erweiterung

Im Ordner `chrome-extension/` findest du eine Version des Passwortgenerators als Chrome-Erweiterung.

### 🔧 Installation:
1. Öffne `chrome://extensions/`
2. Aktiviere **Entwicklermodus**
3. Klicke auf **„Entpackte Erweiterung laden“**
4. Wähle den Ordner `chrome-extension/` aus dem Projekt

Fertig! Du kannst die Erweiterung nun direkt in Chrome verwenden.

---

## 🧪 Beispielausgabe

```
[GUI-Fenster erscheint]
[Länge eingeben: 12]
[Sonderzeichen: ✅]
→ Passwort: g7K#f8!mZxW2

```

---

## 💻 Voraussetzungen

- Python 3
- tkinter (standardmäßig in Python enthalten)
---

## ▶️ Ausführen
'''
python gui_password_generator.py

Oder lade direkt die .exe-Datei herunter (keine Installation von Python nötig):

🔗 **[Zum aktuellen Release auf GitHub](https://github.com/admin-evil/password-generator/releases/latest)**


## 📁 Dateien

- gui_password_generator.py – Hauptprogramm

- README.md – Projektdokumentation

- .gitignore – ignorierte Dateien (z. B. dist/, __pycache__/)

- gui_password_generator.spec – Build-Datei für PyInstaller

---

## 📝 Lizenz

Dieses Projekt steht unter der MIT Lizenz.
