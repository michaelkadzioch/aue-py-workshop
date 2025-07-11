filename = 'test-files/sensordaten.txt'

try:
    open(filename, 'r')
except FileNotFoundError:
    print('Die Datei wurde nicht gefunden.')
else:
    with open(filename, 'r') as file:
        filedata = file.read()

    print(filedata)
    print(type(filedata))

    listeAusDatei = filedata.split(';')

    print(listeAusDatei)

    zahlenliste = []

    for element in listeAusDatei:
        try:
            zahlenliste.append(float(element))
            
        except ValueError:
            print(f'Es wurde keine gültige Zahl in der Datei gefunden: {element}')

    print(zahlenliste)

    zahlenliste.sort()

    print(zahlenliste)
    