#Copyright 2018, Will Kelly, All rights reserved.

#finds the largest number in a list of numbers


#subroutines
def findMax(listNumbers):
    if len(listNumbers) != 0:
        output = listNumbers[0]

        for elmt in listNumbers:
            if output < elmt:
                output = elmt

        return output
    else:
        return "Empty list"

#main program
print(findMax([-3,2,-1, 5]))