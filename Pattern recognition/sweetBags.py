def sweetBags():
    correctInput = False
    while correctInput == False:
        try:
            numBags = int(input("Please enter the number of bags: "))
            numSweets = int(input("Please enter the number of sweats (Note that it must be grater than number of bags): "))
        except:
            print("Incorrect input")
        if numSweets < numBags:
            print("You need to enter a number of sweats greater than the number of bags")

        else:
            correctInput = True


    if (numSweets % 2 == 0 and numBags % 2 !=0 ) or (numBags % 2 == 0 and numSweets % 2 != 0):
        print("This doesn't work!")
    else:
        print("This works!")

# main program
runProgram = True
while runProgram == True:
    sweetBags()
    goAgain = input("Would you like to go again (y/n)? ")
    if goAgain.lower() == "n":
        runProgram = False
        print("Goodbye")
    elif goAgain.lower() != "y" or goAgain.lower() != "n":
        print("Not correct input \nGoing again")
    else:
        print("Ok, Starting again!")
