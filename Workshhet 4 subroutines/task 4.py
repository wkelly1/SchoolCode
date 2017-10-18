# main program
carparkSpaces = {}
def emptyCarPark():
    carparkSpaces = {}
    print("Car park is now empty!")
    #print(carparkSpaces)

def parkACar():
    # takes input of registration and what space it is parked in
    regNumber = input("What is the registration of the car? ")
    space = input("please input the space you have parked the car (row,column)")# "1,4"
    # checks if a car is there
    try:
        if int(space[:space.index(",")]) < 11 and int(space[:space.index(",")]) > -1 and int(space[space.index(",")+1:]) > -1 and int(space[space.index(",")+1:]) < 7:

            for key, value in carparkSpaces.items():
                if value == space:
                    print("Car is already there")
                    space = "full"



            # if not then add the car to the dictionary
            if space != "full":
                carparkSpaces.update({regNumber: space})
                print("Ok, car has been added to list and space is free!")



            print(carparkSpaces)

        else:
            print("That is not a car park space!")

    except:
        print("oops you typed something wrong!")
        print()
def removeACar():
    registration = input("What is the registration of the car you want to remove?")
    try:
        carparkSpaces.pop(registration)
        print("Car removed!")
    except:
        print("That car does not exist in the carpark!")

    #print(carparkSpaces)

def displayCarParkGrid():
    print(carparkSpaces)


#initialise car park grid to “empty”
#display menu of options

print("1. Reset all spaces in the car park to 'empty'")
print("2. Park a car")
print("3. Remove a car")
print("4. Display the car park grid")
print("5. Quit\n")
option = input("Enter your choice: ")
#accept choice
while option != "5":
    if option == "1":
        emptyCarPark()
    elif option == "2":
        parkACar()
    elif option == "3":
        removeACar()
    elif option == "4":
        displayCarParkGrid()
    else:
        option = ("Invalid choice - please re-enter: ")

    print("1. Reset all spaces in the car park to ‘empty’")
    print("2. Park a car")
    print("3. Remove a car")
    print("4. Display the car park grid")
    print("5. Quit\n")
    option = input("Enter your choice: ")
print("Goodbye")
