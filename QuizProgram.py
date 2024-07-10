Quiz_questions = {
    '1.' : {
       "question" : "What is the capital of India?" ,
        "answer" : "Delhi"
    },
    '2.' : {
       "question" : "Who is the Prime Minister of India?" ,
        "answer" : "Narendra Modi"
    },
    '3.' : {
       "question" :  "Who is the captian of Indian cricket team?" ,
        "answer" : "Rohit Sharma"
    },
    '4.' : {
       "question" : "Which country is the native of cricket?" ,
        "answer" :  "England"
    },
    '5.' : {
       "question" :"Where continent is Switzerland located?"  ,
        "answer" : "Europe"
    },
    '6.' : {
       "question" :"Where is Tokyo located?"  ,
        "answer" : "Japan"
    },
    '7.' : {
       "question" :"Who is the father of computer"  ,
        "answer" : "Charles babage"
    },
    '8.' : {
       "question" :"Who is the father of Artificial Intelligence"  ,
        "answer" : "John Mcarty"
    },
}

score = 0

while True:
    print('')
    print("Welcome to the Quiz")
    print('')
    start_input = input("Are you ready to enter into the quiz. Press (y) to continue or (n): ")
    print('')
    
    if start_input.lower() != 'y':
        print("😒😒😒Ohhh!. You have left the quiz")
        break
    else:
        for key, values in Quiz_questions.items():
            print(key,values['question'])
            print('')
            answer = input("Enter the answer: ")
            print('')
            
            if answer.lower() == values['answer'].lower():
                print("😊😊😊Correct")
                print('')
                score += 1
                print("Your Score is "+str(score))
                print('')
            else:
                print("👍Better Luck Next time")
                print('')
                print("The answer is "+values["answer"])
                print('')
                print("Your score is "+str(score))
        break    
                
print("Your final score is ",str(score),'/8')
print('')
print("😉😉😉Quiz complete.Bye Thanks")

