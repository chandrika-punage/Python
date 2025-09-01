import requests
resp=requests.get('https://jsonplaceholder.typicode.com/users')
users=resp.json()
print(users)
print(type(users))   #List

for user in users:
    # print(user['username'])     #prints all the usernames 

    print("User Id:",user['id'],"- Name:",user['username'])




