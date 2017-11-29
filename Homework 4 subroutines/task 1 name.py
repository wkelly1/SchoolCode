#functions

# display menu of options
def displayMenu():
    print("1. Add name\n2. Display list \n3. Quit\n ")
    option = int(input("Enter your choice: "))
    # accept choice
    while option not in range(1,4):
        option = int(input ("Invalid choice - please re-enter: "))
    endwhile
    return optio
    n
endfunction

def addName():
    name = input("What name would you like to add?")
    position = int(input("What position would you like to put the name (1-10)?"))-1
#checks if position is valid
    if position > 0 and position < 11 then
        names.insert(position, name)
    else:
        print("That is not a position between 1 and 10!")
    endif
endfunction

def displayList():
    #checks to see if list is empty and if so prints list is empty
    #This is not explicitly asked for but i thought it might be nice to add
    counter = 1
    for elmt in names:
        if elmt != "" then:
            counter = counter +1
        endif
    next elmt

    if counter > 1 then
        for i in range(10):
            if names[i] then
                print(i + 1, names[i])
            endif
        next i
    else
        print("List is empty!")
    endif
#variables
names = [""]*10

#main program
choice = 0
while choice != 3:
    choice = displayMenu()
    if choice == 1 then
        addName()
    elif choice == 2 then
        displayList()
    else
        print("Goodbye")
    endif
endwhile
