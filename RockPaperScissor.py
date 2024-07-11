import random

print("")
print("----------Rock/Paper/Scissor-Game----------")
print("")
print('''Rules:
    1)The one who scores 10 points first will be considered the winner of the game.
    2)Do not enter invalid input.
    3)Your score will be shown at the end of each round''')
print('')

Player_Score = 0
COmputer_Score = 0
    
while True:
    
    Input_List = ["Rock","Paper","Scissor"]

    Player_Choice = input("Enter Rock/Paper/Scissor/Exit: ")
    
    if Player_Choice.lower() == 'exit':
        print("Your total score: ",Player_Score)
        print('')
        print("Bye Thanks!!")
        print('')
        break
    
    if Player_Choice.capitalize() not in Input_List:
        print("Invalid input. Enter a valid one")
        print("")
        continue
    
    Computer_Choice = random.choice(Input_List)
    
    print('')
    print("You Chose: ",Player_Choice)
    print('')
    print("Computer Chose: ",Computer_Choice)
    
    
    if Computer_Choice.lower() == 'paper' and Player_Choice.lower() == 'scissor':
        print('')
        print("😉😉😉You Win!")
        print('')
        Player_Score += 1
        print('Player-score:',Player_Score)
        print('')
        print("Computer score:",COmputer_Score)
        print('')
    elif Computer_Choice.lower() == 'rock' and Player_Choice.lower() == 'paper':
        print('')
        print("😉😉😉You Win!")
        print('')
        Player_Score += 1
        print('Player-score:',Player_Score)
        print('')
        print("Computer score:",COmputer_Score)
        print('')
    elif Computer_Choice.lower() == 'scissor' and Player_Choice.lower() == 'rock':
        print('')
        print("😉😉😉You Win!")
        print('')
        Player_Score += 1
        print('Player-score:',Player_Score)
        print('')
        print("Computer score:",COmputer_Score)
        print('')
    elif Computer_Choice.lower() == Player_Choice.lower():
        print('')
        print("💪💪💪Tie Match")
        print('')
        print('Player-score:',Player_Score)
        print('')
        print("Computer score:",COmputer_Score)
        print('')
    else:
        print('')
        print("🙂🙂🙂Computer Wins")
        print('')
        COmputer_Score += 1
        print('Player-score:',Player_Score)
        print('')
        print("Computer score:",COmputer_Score)
        print('')
        
    if Player_Score == 10:
        print("")
        print("You win")
        print("")
        break
    elif COmputer_Score == 10:
        print("")
        print("Game Over!!!")
        print("Computer wins.Better luck next time.")
        print("")
        break 