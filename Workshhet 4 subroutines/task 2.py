#checks validity of passwords before allowing it to be changed

def getPword(attempt):
    if attempt == 1:
        password = input("Please input your password (6-8 characters): ")
        return password
    elif attempt == 2:
        password = input("Please input your password again: ")
        return password
    else:
        print("Too many attempts!")

#main program
password1 = getPword(1)
password2 = getPword(2)

if password1 != password2:
    print("passwords are not the same!")
elif len(password1) <6 or len(password1) >9:
    print("password is not the correct length!")
else:
    print("password has been changed!")
