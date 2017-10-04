i = True
noOldParts = 0
while i == True:
    number = input("Please input a part number")
    if len(number) != 4:
        print("Input the number again, wrong length")
    elif number == "9999":
        print("9999 is too high")
        i = False
    elif number[3] == "6" or "7" or "8":
        noOldParts = noOldParts + 1
    else:
        partNo = partNo + 1

    print("number of old parts = ", noOldParts)
