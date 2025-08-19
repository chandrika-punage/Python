# WAP-check given number is even or odd

num=int(input("Enter the number: "))
if num%2==0:
    print("Number is even")
else:
    print("number is odd")

    

# Enter the number: ten   #ValueError: invalid literal for int() with base 10: 'ten'
# cannot convert ten(str) into the int type