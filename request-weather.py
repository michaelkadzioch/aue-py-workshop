import requests

url = 'https://api.open-meteo.com/v1/forecast'

# response = requests.get(url, headers=headers)

parameter = { 
    'latitude': 50.1,
    'longitude': 8.64,
    'current': 'temperature_2m'
    }

response = requests.get(url, params=parameter)

print(response.status_code)
print(response.content)

data = response.json()

print('Aktuelle Temerpatur: ' + str(data['current']['temperature_2m']))


    