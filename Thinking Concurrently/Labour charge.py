#finds charge from a duration of time

#functions
def labourCharge(duration):
    time = int(duration) / 30
    if int(duration) % 30 != 0:
        charge = (int(str(time)[:str(time).index(".")])*20)+20
    else:
        charge = time * 20
    return charge

charge = "0120"
print(labourCharge(charge))

