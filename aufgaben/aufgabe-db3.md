# Aufgabe Datenbank 3

Name, Passhash und Id eines bestimmten Users sollen aus der Datenbank gelesen werden und dannach in einer JSON-Datei gespeichert werden.
Die Jsondatei sollen dazu die Keys "id", "user" und "accesscode".

Der Username soll dabei durch eine Benutzereingabe entgegen genommen werden.

Das Programm soll folgende Fehler erkennen und eine Fehlerbehandlung ausfüheren (z.B. Ausgabe Fehlermeldung):

- Datenbankbindung kann nicht Aufgebau werden
- Datensätze können nicht lesen werden.
- Datensätze können nicht gefunden werden (z.B. User in der Datenbank nicht vorhanden)
- JSON-Datei kann nicht geöffnet / geschrieben werden.


Zur Datenbankabfrage soll eine SQL-Statment mit Where-Kausel verwendet werde.

Code-Beispiel:

    sql = "SELECT * FROM user WHERE username = %s"
    username = ("Hugo", )

    mycursor.execute(sql, username)

Das Progamm soll Funktionen und Clean-Code beinhalten.