#finds charge from a duration of time

#functions
def labourCharge(duration):
    time = int(duration) / 30
    if time != 0:
        charge = (int(str(time)[:str(time).index(".")])*20)+20
    else:
        charge = time * 20
    return charge

#main program
charge = "0110"
print(labourCharge(charge))
