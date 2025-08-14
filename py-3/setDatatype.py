#Create

s1={}               #dict type
print(type(s1))     


s2=set()
s3={10,20,30,40}
s4={10,10,10,20}
s5={10,20.5,True}

print(s4)           #{10, 20}
print(s5)           #{True, 10, 20.5}


#Update

s5.add("John")
print(s5)           #{True, 10, 'John', 20.5}


# ---------------------------------------------------------
eids={101,102,103,104}

#we cannot use indexing method to get the elements
# print(eids[0])      #TypeError: 'set' object is not subscriptable

#How to read set value-->using for loop

for eid in eids:
    print(eid)