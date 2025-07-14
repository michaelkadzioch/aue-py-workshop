import json

data = {
  'name': 'Hans',
  'age': 30,
  'city': 'Berlin'
}

jsondata = json.dumps(data)

print(jsondata)