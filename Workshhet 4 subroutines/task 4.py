# main program
def emptyCarPark(carPark):

def parkACar(carPark):
    regNumber = input("What is the registration of the car? ")
    space = input("please input the space you have parked the car (row,column)")

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
        emptyCarPark(carPark)
    elif option == "2":
        parkACar(carPark)
    elif option == "3":
        removeACar(carPark)
    elif option == "4":
        displayCarParkGrid(carPark)
    else:
        option = ("Invalid choice - please re-enter: ")
    print("1. Reset all spaces in the car park to ‘empty’")
    print("2. Park a car")
    print("3. Remove a car")
    print("4. Display the car park grid")
    print("5. Quit\n")
    option = input("Enter your choice: ")
print("Goodbye")
