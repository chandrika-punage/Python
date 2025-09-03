# def login():
#     print("Login Success")

# login()
# login()
# login()

# -----------------------------------------------------------------

# def add():
#     print("Addition")

# add(10,20)      #TypeError: add() takes 0 positional arguments but 2 were given

# -----------------------------------------------------------------


def add(a,b):       #a,b are the arguments
    print(a+b)

add(10,20)  #30
add(2,3)    #5
add("John","Doe")  #JohnDoe
add(10,20,30)   #TypeError: add() takes 2 positional arguments but 3 were given
add("john",10)      #TypeError: can only concatenate str (not "int") to str
# add(1)  #TypeError: add() missing 1 required positional argument: 'b'
# add() # TypeError: add() missing 2 required positional arguments: 'a' and 'b'
# sub()   #NameError: name 'sub' is not defined. Did you mean: 'sum'?


# -----------------------------------------------------------------

# emp={
#     "eid":101,
#     "name":"John"
# }

# print(emp['eid'])       #101
# print(emp['loc'])       #KeyError: 'loc'


# -----------------------------------------------------------------

