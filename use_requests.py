import requests

URL = "https://jsonplaceholder.typicode.com/posts"

params = {"userId": 1}

# obtenemos los posts del userId 1
response = requests.get(URL, params)

print(response.json())
