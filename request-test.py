import requests

url = 'https://www.tagesschau.de/api2u/homepage/'

# response = requests.get(url, headers=headers)
response = requests.get(url)

print(response.status_code)
# print(response.content)

data = response.json()

news = data['news']

for element in news:
    print('--------')
    print(element['date'])
    print(element['title'])
    print(element['topline'])
    