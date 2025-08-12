price=399                   #int
rating=4.1                  #float
branc_name="TB blue"        #str
prod_name='Pen'             #str
avail=False                 #bool
c=10+20j                    #complex
colors=["red","orange","blue"]  #list
eids=(101,102,103,104)          #tuple
uids={101,102,103,104}          #set
specialization={                #dict(grp of key value pairs)
    'size':38,
    'fits':"Regular"
}


#--------------type func returns the datatype


print(type(price))
print(type(rating))
print(type(branc_name))
print(type(prod_name))
print(type(avail))
print(type(c))
print(type(colors))
print(type(eids))
print(type(uids))
print(type(specialization))     



#--------------------------------------------------

l=[18,31,7,8,11,232,55]

b=bytes(l)          #byte
ba=bytearray(l)     #butearray
fz=frozenset(l)     #frozenset
r=range(100)        #range
nt=None             #NoneType

print(type(b))
print(type(ba))
print(type(fz))
print(type(r))
print(type(nt))