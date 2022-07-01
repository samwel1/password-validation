import re


password = input("Enter password:")

x = True

while x:
    if (len(password)<8 or len(password)>20):
        break
    elif not re.search("[a-z]",password):
        break
    elif not re.search("[0-9]",password):
        break
    elif not re.search("[^A-Z", password):
        break
    elif not re.search("[$#@]", password):
        break
    elif not re.search("\s", password):
        break
    else:
        print("Valid Password")
        x = False
        break
    if x:
        print("Not a valid Password")
