# Aufgabe Datenbank 2

Name und Passhash sollen aus einer Jsondatei entgegen genommen werden und in der Datenbank gepeichert werden.
Die Jsondatei enthält dazu die beiden Keys "user" und "accesscode".

Zur Überprüfung soll der Inhalt der Datenbank ausgelesen und ausgeben werden.

Das Programm soll folgende Fehler erkennen und eine Fehlerbehandlung ausfüheren (z.B. Ausgabe Fehlermeldung):

- Datenbankbindung kann nicht Aufgebau werden
- Datensätze können nicht in die Datenbank geschrieben werden.
- JSON-Datei kann nicht geöffnet werden.
- JSON-Datei fehlerhalt oder unvollständig (z.B. Keys fehlen)

Das Progamm soll Funktionen und Clean-Code beinhalten.