import random 
import time

print('')
print("Welcome to Timed Math Challenge")
print('')

OPERATORS = ['+','-','*']
MIN_NUMBER = 2
MAX_NUMBER = 12
TOTAL_QUESTIONS = 10

def problem_generator():
    left_input = random.randint(MIN_NUMBER,MAX_NUMBER)
    right_input = random.randint(MIN_NUMBER,MAX_NUMBER)
    operator = random.choice(OPERATORS)
    
    expression = str(left_input) + " " + operator + " " + str(right_input)
    answer = eval(expression)
    return expression, answer

wrong = 0
input("Press enter to start")
print('')
print('Your time starts now')
print('-------------------------------')

start_time = time.time()

for i in range(TOTAL_QUESTIONS):
    expression, answer = problem_generator()
    while True:
         guess = input("Problem #" + str(i+1) + ': ' + expression + ' = ')
         if guess == str(answer):
               break
         wrong += 1  
         
end_time = time.time() 
total_time = round(end_time - start_time, 2)

print('')
print("You had "+str(wrong)+" questions wrong.")
print('')
print("You completed it in "+ str(total_time) + " seconds")
print('')
print('🎊🎊🎊You rocked it.')
         
print('-------------------------------')  