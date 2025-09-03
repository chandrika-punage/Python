
#############How to invoke inner function from outside?

def user_module(name,status):

    def login():
        print("Login Success")

    def logout():
        print("Logout Success")
        
    if status==True:
        return login
    else:
        return logout
        
inner=user_module("Ab",False)            
inner()             #Logout Success


