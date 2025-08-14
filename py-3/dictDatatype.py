#Create

d1={}

emp={
    "eid":101,
    "ename":"John",
    "esal":45000.45
}

user={
    "uid":101,
    "uid":102,
    "uid":103,
    "uid":104,
    "uid":105

}


#Read


print(d1)       #{}
print(emp)      #{'eid': 101, 'ename': 'John', 'esal': 45000.45}

print(user)     #{'uid': 105} -->its going to override becoz duplicates r not allowed



#How to read Dict Values?-->using keys

print(emp['eid'])           #101
print(emp['ename'])         #John
print(emp['esal'])          #45000.45
# print(emp['Loc'])        #it is not present so it gives error--> KeyError: 'Loc'



#Update

emp['ename']='John Doe'
print(emp)          #{'eid': 101, 'ename': 'John Doe', 'esal': 45000.45}
print(emp['ename'])     #John Doe


#Adding new Element

emp['email']="JohnDoe@gmail.com"
print(emp['email'])                     #JohnDoe@gmail.com    it got added in the emp 




#Delete

del emp['esal']
print(emp)              #{'eid': 101, 'ename': 'John Doe', 'email': 'JohnDoe@gmail.com'}




#----------------------------------------------------------------


# Example 


#Create

Product={
    "pid":101,
    "pname":"Alice",
    "price":30,
    "details":{
                "color":"Blue",
                "size":"Small",
                "avial":True
    },          #if we don't give comma here it gives error--> SyntaxError
    "another":{
                "listofcolor":["red","yellow","orange","pink"]  #its list indexing is allowed
                #['red', 'yellow', 'orange', 'pink']


            
    }
}


#Read

print(Product["pname"])     #Alice
print(Product['details']['color'])      #Blue
print(Product['details']['size'])       #small



print(Product['another']['listofcolor'])
print(Product['another']['listofcolor'][1])   #yellow
print(Product['another']['listofcolor'][3])    #pink





