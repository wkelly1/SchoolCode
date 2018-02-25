#The creator of the quiz would have to fill this information in with 10 questions and 40 answers
quizQuestionsAnswers = {"Q1":["A1","A2","A3","A4"],
                        "Q2":["A1","A2","A3","A4"],
                        "Q3": ["A1", "A2", "A3", "A4"],
                        "Q4": ["A1", "A2", "A3", "A4"],
                        "Q5": ["A1", "A2", "A3", "A4"],
                        "Q6": ["A1", "A2", "A3", "A4"],
                        "Q7": ["A1", "A2", "A3", "A4"],
                        "Q8": ["A1", "A2", "A3", "A4"],
                        "Q9": ["A1", "A2", "A3", "A4"],
                        "Q10": ["A1", "A2", "A3", "A4"],
                        }

correctQuestion = [1,3,2,2,3,1,3,2,1,4]

quizAsciiArt = """
             _     
            (_)    
  __ _ _   _ _ ____
 / _` | | | | |_  /
| (_| | |_| | |/ / 
 \__, |\__,_|_/___|
    | |            
    |_| 
"""
#functions
def questions(quizQuestionsAnswers, correctQuestion):
    noCorrectAnswers = 0
    for key, value in quizQuestionsAnswers.items():
        print("question: "+key)
        print("These are your answer options: ")
        for i in value:
            print(i)
        answer = findAnswer()

        keys = list(quizQuestionsAnswers)
        currentQuestion = keys.index(key)

        if int(answer) == int(correctQuestion[currentQuestion]):
            print("correct\n")
            noCorrectAnswers = noCorrectAnswers +1
        else:
            print("incorrect\n")
    return noCorrectAnswers

def findAnswer():
    moveOn = False
    while moveOn == False:
        answer = input("What is your answer? (1-4)")
        try:
            int(answer)
            if int(answer) < 5 and int(answer) > 0:
                moveOn = True
            else:
                print("oops you've entered something wrong!")
        except:
            print("oops you've entered something wrong!")

    return answer
#main program
goAgain = "y"
while goAgain.lower() == "y":
    print(quizAsciiArt)
    print("This is the quiz - have fun!")
    print("Number of correct questions:", questions(quizQuestionsAnswers, correctQuestion))
    correctInput = False
    while correctInput == False:
        goAgain = input("Would you like to play again? (y/n)")
        if goAgain == "y" or goAgain == "n":
            correctInput = True
        else:
            print("oops you've entered the wrong thing")
            correctInput = False

print("Thanks for playing!!")
