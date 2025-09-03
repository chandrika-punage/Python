# def outer():
#     print("Outer func")

#     def inner():
#         print("Inner func")

# outer()
# inner()


# we get error:::::::
#  inner()
#     ^^^^^
# NameError: name 'inner' is not defined.

# ----------------------------------------------------------------------------

# def outer():
#     print("Outer func")

#     def inner():
#         print("Inner func")
#     inner()
#     inner()

# outer()

# # Output::
# # Outer func
# # Inner func
# # Inner func


# ----------------------------------------------------------------------------



#############How to invoke inner function from outside?


def user_module():
    print("Outer function")

    def login():
        print("Login Success")

    def logout():
        print("Logout Success")
        
    return 100


x=user_module()
print(x)



