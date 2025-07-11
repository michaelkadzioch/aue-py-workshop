import json

filename = 'json-files/test1.json'

try:
    open(filename, 'r')
except FileNotFoundError:
    print('Die Datei wurde nicht gefunden.')
else:
    with open(filename, 'r') as file:
        filedata = file.read()

    
    print(filedata)
    print(type(filedata))

    jsondata = json.loads(filedata)
    print(jsondata)
    print(type(jsondata))