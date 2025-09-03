
#############How to invoke inner function from outside?


def user_module():
    print("Outer function")

    def login():
        print("Login Success")

    def logout():
        print("Logout Success")
        
    return login


x=user_module()
print(type(x))  #<class 'function'>
print(x)        #<function user_module.<locals>.login at 0x0000022D727AC0E0>
x()             #Login Success


# --------------------------------------------------------------------------------------

def user_module():
    print("Outer function")

    def login():
        print("Login Success")

    def logout():
        print("Logout Success")
        
    return login
    return logout


inner=user_module()
print(type(inner))   #<class 'function'>    
inner()             #Login Success
inner()             #Login Success
inner()             #Login Success
