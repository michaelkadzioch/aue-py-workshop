import requests

url = 'https://www.tagesschau.de/api2u/news/'

# response = requests.get(url, headers=headers)

parameter = { 
    'regions': 8,
    'ressort': 'sport'
    }

response = requests.get(url, params=parameter)

print(response.status_code)
# print(response.content)

data = response.json()

news = data['news']

for element in news:
    print('--------')
    print(element['date'])
    print(element['title'])
    print(element['topline'])
    