def multiples(table, startnum, endnum, pupilName):
    print("Hi", pupilName, "…here is your timetable")
    for i in range(startnum, endum):
        print(table * i)


name = input("what is your name?")
table = input("Enter your time table?")
startnum = input("what is your start number?")
endnum = input("What is your end number?")

multiples(table, startnum, endnum, name)
