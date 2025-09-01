import requests

resp=requests.get('https://dummyjson.com/products')
prod=resp.json()
print(prod)

for product in prod:
    