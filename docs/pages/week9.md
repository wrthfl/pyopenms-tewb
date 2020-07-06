# Woche 9

1. Arbeitet eventuelle Rückstände auf:
    - Änderungen des Experimental Design Widget:
        - Die Spalten lassen sich nun sortieren
        - Tabelle kann nun gefiltert werden indem man den Suchbegriff im Textfeld
            eingibt

    - Änderungen des XML configuration Widget:
        - Die XML wird vor dem parsen defused (gegen xmlattacks)
        - Die Spalte value lässt sich nun editieren:
            - Andere Spalten geben einen Error wenn sie versucht werden zu editieren
            - Neuer Wert muss dem angegeben Typ entsprechen
            - Restrictions werden überprüft und neuer Wert muss diesen entsprechen
        - Jede Änderung wird im eTree model gespeichert
        - eTree model kann gespeichert werden als XML .ini Datei
        - Einige andere Refactorings um den Code zu verbessern
            - Aus der Initialisierung wurden einige Methoden extrahiert
            - Das TreeWidget wird nun rekursiv gezeichnet
            
    - generelles Aufräumen wie ungenutzte Imports rausschmeissen, ...
    
 2. Bugs
    - Fraction und Label besitzten derzeit noch ein seltsames Verhalten(der Eintrag in entsprechender Spalte wird nicht überall korrekt gesetzt)
    (- XMLs werden noch nicht default als ini gespeichert (.ini muss immer noch manuel hinter den Dateinamen gesetzt werden))
