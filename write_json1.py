import json

meindict = {
    'name': 'Max', 
    'alter': 35
    }

json_string = json.dumps(meindict)

neue_json_datei = open('meindict.json', 'wt')
neue_json_datei.write(json_string)