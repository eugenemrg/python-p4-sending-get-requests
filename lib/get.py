import requests
import json

url = 'https://dummyjson.com/products?limit=10&skip=10&select=title,price'

response = requests.get(url)

json_content = json.loads(response.text)

print(json.dumps(json_content, indent=4))
