class Dog():
    def __init__(self, myName, myColour):
        self.__name = myName
        self.__colour = myColour

    def bark(self, numTimes):
        for i in range(0,numTimes):
            print("Woof!")


dog1 = Dog("bob","brown")
dog1.bark(2)


class Puppy(Dog):
    def __init__(self, myName, myColour):
        person.__init__(self, myName, myColour)
        self.__name = myName
        self.__colour = myColour
