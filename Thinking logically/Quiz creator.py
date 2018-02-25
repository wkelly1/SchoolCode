#Creates the correct data layout for the quiz
quizQuestionsAnswers = {}
correctQuestion = []

moveOn = False
while moveOn == False:
    noQuestions = input("How many questions do you want? ")
    try:
        int(noQuestions)
        if int(noQuestions) < 5 and int(noQuestions) > 0:
            moveOn = True
        else:
            print("oops you've entered something wrong!")
    except:
        print("oops you've entered something wrong!")


for i in range(int(noQuestions)):
    question = input("What is your question no.{}? ".format(i+1))
    answer1 = input("What is your first possible answer?")
    answer2 = input("What is your second possible answer?")
    answer3 = input("What is your third possible answer?")
    answer4 = input("What is your fourth possible answer?")
    moveOn = False
    while moveOn == False:
        correct = input("Which one of those is the correct answer? (1-4)")
        try:
            int(correct)
            if int(correct) < 5 and int(correct) > 0:
                moveOn = True
            else:
                print("oops you've entered something wrong!")
        except:
            print("oops you've entered something wrong!")
    correctQuestion.append(int(correct))
    print(correctQuestion)
    quizQuestionsAnswers.update({question: [answer1, answer2, answer3, answer4]})
    print(quizQuestionsAnswers)