password = input("Enter your password: ")
l = len(password)
if l < 8:
    print("Invalid password")
else:
    digit = False
    upper = False
    lower = False
    special = False  
    for i in password:
        if i.isdigit():  
            digit = True
        elif i.isupper():  
            upper = True
        elif i.islower():  
            lower = True
        elif not i.isalnum():
            special = True
    if digit and upper and lower and special:
        print("Valid password")
    else:
        print("Invalid password")
