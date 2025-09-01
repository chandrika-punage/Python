import requests

resp=requests.get('https://dummyjson.com/products')
prod=resp.json()
print(type(prod))       #<class 'dict'>
# print(prod)
print(resp.status_code)     #200(Success)


products=prod['products']
print(type(products))           #<class 'list'>
print(len(products))        #30




    