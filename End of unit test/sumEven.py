#subroutines
def sumEven(number):
    if number%2 == 0:
        sum = number
        while number!=0:
            number = number -2
            sum = sum + number
        return sum
    else:
        number = number -1
        sum = number
        while number!=0:
            number = number -2
            sum = sum + number
        return sum

#main program
print(sumEven(12))