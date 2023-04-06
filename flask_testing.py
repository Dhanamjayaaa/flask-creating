import requests

data = requests.get(r'http://127.0.0.1:5000/players_id?id=1')
print(data.content)