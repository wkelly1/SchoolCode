def findMax(listNumbers):
    if len(listNumbers) != 0:
        output = listNumbers[0]

        for elmt in listNumbers:
            if output < elmt:
                output = elmt

        return output
    else:
        return "Empty list"


print(findMax([-3,2,-1, 5]))