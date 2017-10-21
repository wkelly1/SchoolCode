names = []

#functions
def addName():
    name = input("What name would you like to add?")
    position = int(input("What position would you like to put the name (1-10)?"))

    if position > 0 and position < 11:
        names.insert(position, name)
    else:
        print("That is not a position between 1 and 10!")


def displayList():
    print(names)
    for elmt in names:
        print(names.index(elmt) +1, elmt)


#main program

# display menu of options

print("1. Add name")
print("2. Display list")
print("3. Quit\n")
option = input("Enter your choice: ")
# accept choice
while option != "3":
    if option == "1":
        addName()
    elif option == "2":
        displayList()
    else:
        option = ("Invalid choice - please re-enter: ")

    print("1. Add name")
    print("2. Display list")
    print("3. Quit\n")
    option = input("Enter your choice: ")
print("Goodbye")