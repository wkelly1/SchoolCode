#subroutines
def responseYorN():
    response = input("input your response: ")
    if response == "y" or response == "n":
        print("valid")
    else:
        print("invalid")

#main program
responseYorN()