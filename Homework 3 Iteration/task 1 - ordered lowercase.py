#order an inputted list from smallest (a) to largest (z) #
# Then print first and last element

letters = []
for i in range(0,5):
    #run a check on the input
    command = True
    while command == True:
        try:
            info = input("Please input your next letter (1 character): ")
            int(info)
            print("This is not a letter")
        except:
            if len(info) != 1:
                print("Not a single letter!")
            else:
                letters.append(info)
                command = False

#printing/sorting inputs
letters = sorted(letters)
print(letters)
print("smallest:", letters[0], "and largest:", letters[-1])
