#Check password and allow for 3 attempts

i = 0
continueOn == True
while i < 3 AND continueOn == True: #added continueOn to stop the program when pass is correct
    password = input("Please input your password: ")
    if password == "Tues1212":
        print("Password accepted")
        continueOn == False
    else:
        print("Password rejected")
        i = i+1

print("cooll")

