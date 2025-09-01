
import requests
resp=requests.get('https://dummyjson.com/products')
product_data=resp.json()
products=product_data['products']


#Using for Loop
for product in products:
    if product['category'] =='beauty':
        print(product['title'])




