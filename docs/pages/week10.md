# Woche 10

1. Arbeitet eventuelle Rückstände auf:
    - Drag and Drop für die Configview wurde implementiert, jedoch funktioniert das parsen trotz exakt gleichen Pfad nicht
        - Bug in pyqt oder etree?
    - Das Verhalten des ConfigView Widgets wurde so verändert, dass nun die Itemlists veränderbar sind und auch Items hinzugefügt werden können mithilfe eines add buttons. Dieser checkt die angegeben restrictions und types für den neuen Wert.
    ![alt text](../Screenshots/AddParameter.png )

2. Neues:
    - Run Menü wurde hinzugefügt. In diesem gibt es die Option über das Terminal welches die Final Box.py laufen lässt einen Befehl auszuführen.
     Momentan wird erstmal nur der Beispiel Code aus dem Wochenplan 10 hardcoded ausgeführt.
3. Probleme:
    - der Befehl erzeugt noch einen Fehler(noch keine Lösung gefunden)
    ![alt text](../Screenshots/error.png )
    - bisher nur auf Windows getestet
