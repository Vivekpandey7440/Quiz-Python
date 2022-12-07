import random
import json

def str2bool(v):
  return v.lower() in ("yes", "true", "t", "1", "y")


class Quiz:
    def init():
        """Initialize the quiz"""
        global IncorrectScore
        global CorrectScore 
        global questions

        IncorrectScore = 0
        CorrectScore = 0

        questions = Quiz.loadQuestions()
        category = Quiz.showCatalogs()
        if category  == -1:
            Quiz.init()
            return
        elif(category == 0):
            quizQues = Quiz.pickRandomMergedQuestions()
        else:
            quizQues = Quiz.pickRandomQuestions(category)
        Quiz.startTest(quizQues)
        Quiz.endTest()

    def loadQuestions():
        """Loads questions from json file in a dictionary."""
        with open('src/questions.json', 'r', encoding="utf8") as file:
            quesDict = json.load(file)

        return quesDict


    def showCatalogs():
        """Shows the availaboe categories to the user and allows them to pick one among them"""
        categories = list(questions.keys())
        for i in range(0, len(categories)):
            print("%d. %s"%(i+1, categories[i]))
        print("%d. All In One"%(len(categories) + 1))
        n = int(input(("Choose a category (1-%d): "%((len(categories)+1)))))

        if n < 1 or n > len(categories)+1:
            print("Please select a valid categories in range 1 to %d."%(len(categories)+1))
            return -1
        elif n == len(categories) + 1:
            return 0
        else:
            return categories[n-1]

    def pickRandomMergedQuestions():
        """Merges all the categories and random picks 5 questions from them."""
        quizCategory = list(questions.keys())
        quizQuestions = list()
        for i in quizCategory:
            qIds = list(questions[i].keys())
            for j in qIds:
                question = questions[i][j]["Q"]
                answer = questions[i][j]["A"]

                templist = list()
                templist.append(question)
                templist.append(answer)
                quizQuestions.append(templist)
        
        pickedQues = random.sample(range(0, len(quizQuestions)), 5)

        quesData = list()
        
        
        for i in pickedQues:
            question = quizQuestions[i][0]
            answer = quizQuestions[i][1]

            templst = list()
            templst.append(question)
            templst.append(answer)
            quesData.append(templst)
        
        return quesData

    def pickRandomQuestions(category):
        """Picks 5 random questions from the category mentioned as first parameter."""
        ques = questions[category]
        qIds = list(ques.keys())

        pickedQues = random.sample(range(0, len(qIds)), 5)

        quesData = list()
        for i in pickedQues:
            question = ques[qIds[i]]["Q"]
            answer = ques[qIds[i]]["A"]

            templist = list()
            templist.append(question)
            templist.append(answer)
            quesData.append(templist)

        return quesData
    
    def startTest(question):
        """Starts the test and ask user each questions as passed in list as first parameter."""
        for ques in question:
            response = input("%s\nTrue/False (T/F): "%(ques[0]))
            global IncorrectScore
            global CorrectScore
            if(str2bool(response) == ques[1]):
                CorrectScore += 1
            else:
                IncorrectScore += 1
    
    def endTest():
        """Ends the test and displays the score. Also asks the user for a rematch."""
        global IncorrectScore
        global CorrectScore

        print("Score: %.1f"%((CorrectScore / (CorrectScore+IncorrectScore)) * 100)+"%")
        print("Correct Score:", CorrectScore)
        print("Incorrect Score:", IncorrectScore)

        replay = input("Do you want to play again? (Y/N): ")
    
        if(str2bool(replay) == True):
            Quiz.init()
            return
        else:
            print("Thanks for playing our quiz game. Have a nice day!")
            return

Quiz.init()



