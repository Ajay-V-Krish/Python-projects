import random

print('')
print("-----Pig-Game-----")
print('')
print('''
Rules:
    1)You have to choose the number of players to play the game(2-4).
    2)You can roll the dice as many times as you can.
    3)If you roll one(1) your score will be zero and your chance will be over.
    4)Or else your score will be increasing.
    5)The first player to take 50 points is the winner of the game.''')
print('')
print('Let"s Start🏆🏆🏆')

def roll():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value, max_value)
    
    return roll

while True:
    players = input("Enter the number of players (2-4): ")
    if players.isdigit():
        players = int(players)
        if 2<= players <=4:
            break
        else:
            print("Players should be 2-4")
    else:
        print("Inavlid input")
        

max_score = 50
player_scores = [0 for i in range(players)]

while max(player_scores) < max_score:
    
    for player_idx in range(players):
            print("\nThe Player ",player_idx+1," turn has just started\n")
            print("Your total score is", player_scores[player_idx],'\n')
            current_score = 0
            
            while True:
    
                    need_to_roll = input("If you need to roll press (y) if not press (n): ")
                    if need_to_roll.lower() != 'y':
                            break 
    
                    value = roll()  
                    if value == 1:
                        current_score = 0
                        print("You rolled one! Your turn is over\n")
                        break
                    else:
                         current_score += value
                         print("You rolled a: ", value,'\n')
        
                    print("Your current score is: ", current_score,'\n')

            player_scores[player_idx] += current_score
            print('Your total score is: ',player_scores[player_idx],'\n')
            
max_score = max(player_scores)
winner_idx = player_scores.index(max_score)

print("The winner is player: ",winner_idx+1," with the winning score of: ", max_score)