test1 = []
test2 = []
test3 = []
noPupils = 5
i=0
while i < noPupils:
    input1 = input("Please input first score of test1: ")
    test1.append(int(input1))
    i =i+1
i=0
while i < noPupils:
    input2 = input("Please input first score of test2: ")
    test2.append(int(input2))
    i =i+1
i=0
while i < noPupils:
    input3 = input("Please input first score of test3: ")
    test3.append(int(input3))
    i =i+1

print(test1, test2, test3)


def testAverage(test):
    average = 0
    for elmt in test:
        print(elmt)
        average = average + elmt
        print(average)

    average = average / noPupils
    return average

average1 = testAverage(test1)
average2 = testAverage(test2)
average3 = testAverage(test3)

def fullAverage(average1, average2, average3):
    average = (average1 + average2 + average3)/3
    return average

print("test1 average: ", testAverage(test1))
print("test1 average: ", testAverage(test2))
print("test1 average: ", testAverage(test3))