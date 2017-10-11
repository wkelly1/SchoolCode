def multiples(table, startnum, endnum, pupilName):
    print("Hi", pupilName, "…here is your timetable")
    for i in range(startnum, endnum+1):
        print(table * i)

#main program
name = input("what is your name?")
table = int(input("Enter your time table?"))
startnum = int(input("what is your start number?"))
endnum = int(input("What is your end number?"))

multiples(table, startnum, endnum, name)
