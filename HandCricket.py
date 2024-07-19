# import random

# def player_bat(PLAYER_SCORE, COMPUTER_SCORE):
#     while True:
#         score_input = input('Enter your number (1-10): ')
#         computer_input = random.randint(0, 10)
#         if score_input.isdigit():
#             score_input = int(score_input)
#             if 0 <= score_input <= 10:
#                 if score_input != computer_input and computer_input != 0:
#                     PLAYER_SCORE += score_input
#                     print(f'Your score is {PLAYER_SCORE}')
#                     if PLAYER_SCORE > COMPUTER_SCORE:
#                         print('You win by 10 wickets!')
#                         break
#                 elif score_input == 0:
#                     PLAYER_SCORE += computer_input
#                     print(f'Your score is {PLAYER_SCORE}')
#                     if PLAYER_SCORE > COMPUTER_SCORE:
#                         print('You win by 10 wickets!')
#                         break
#                 else:
#                     print(f'You chose {score_input}')
#                     print(f'Computer chose: {computer_input}')
#                     print('You are out!!!')
#                     print(f'Your total score is {PLAYER_SCORE}')
#                     if PLAYER_SCORE < COMPUTER_SCORE:
#                         print(f'Computer wins by {COMPUTER_SCORE - PLAYER_SCORE}')
#                     break
#             else:
#                 print('Your input should be between 0-10')
#         else:
#             print('Enter a valid number')

# def computer_bat(PLAYER_SCORE, COMPUTER_SCORE):
#     while True:
#         score_input = input('Enter your number (1-10): ')
#         computer_input = random.randint(0, 10)
#         if score_input.isdigit():
#             score_input = int(score_input)
#             if 0 <= score_input <= 10:
#                 if score_input != computer_input and computer_input != 0:
#                     COMPUTER_SCORE += computer_input
#                     print(f'Computer\'s score is {COMPUTER_SCORE}')
#                     if COMPUTER_SCORE > PLAYER_SCORE:
#                         print('Computer wins by 10 wickets.')
#                         break
#                 elif computer_input == 0:
#                     COMPUTER_SCORE += score_input
#                     print(f'Computer\'s score is {COMPUTER_SCORE}')
#                     if COMPUTER_SCORE > PLAYER_SCORE:
#                         print('Computer wins by 10 wickets.')
#                         break
#                 else:
#                     print(f'You chose {score_input}')
#                     print(f'Computer chose: {computer_input}')
#                     print('Computer is out!!!')
#                     print(f'Computer\'s total score is {COMPUTER_SCORE}')
#                     if COMPUTER_SCORE < PLAYER_SCORE:
#                         print(f'Player wins by {PLAYER_SCORE - COMPUTER_SCORE} runs')
#                     break
#             else:
#                 print('Your input should be between 0-10')
#         else:
#             print('Enter a valid number')

# def play_innings(bat_ball_input, PLAYER_SCORE, COMPUTER_SCORE):
#     if bat_ball_input.lower() == 'bat':
#         while True:
#             computer_input = random.randint(0, 10)
#             score_input = input('Enter your number (1-10): ')
#             if score_input.isdigit():
#                 score_input = int(score_input)
#                 if 0 <= score_input <= 10:
#                     if score_input != computer_input and score_input != 0:
#                         PLAYER_SCORE += score_input
#                         print(f'Your score is {PLAYER_SCORE}')
#                     elif score_input == 0:
#                         PLAYER_SCORE += computer_input
#                         print(f'Your score is {PLAYER_SCORE}')
#                     else:
#                         print(f'You chose {score_input}')
#                         print(f'Computer chose: {computer_input}')
#                         print('You are out!!!')
#                         print(f'Your total score is {PLAYER_SCORE}')
#                         print(f'Computer needs {PLAYER_SCORE} runs to win.')
#                         input('Press enter to start bowling.')
#                         computer_bat(PLAYER_SCORE, COMPUTER_SCORE)
#                         break
#                 else:
#                     print('Your input should be between 0-10')
#             else:
#                 print('Enter a valid number')
#     else:
#         computer_bat(PLAYER_SCORE, COMPUTER_SCORE)

# def toss(player_toss_input, computer_toss_input, player_odd_even):
#     player_wins = ((int(player_toss_input) + int(computer_toss_input)) % 2 != 0 and player_odd_even == 'o') or ((int(player_toss_input) + int(computer_toss_input)) % 2 == 0 and player_odd_even == 'e')
#     if player_wins:
#         print(f'Computer input: {computer_toss_input}')
#         print('Player wins')
#         bat_ball_input = input('What do you choose Bat/Bowl: ')
#         play_innings(bat_ball_input, 0, 0)
#     else:
#         print(f'Computer input: {computer_toss_input}')
#         print('Computer wins')
#         computer_choice = random.choice(['bat', 'bowl'])
#         print(f'Computer chose to {computer_choice}')
#         play_innings(computer_choice, 0, 0)

# def main():
#     name = input('Enter your name: ')
#     print(f'Welcome to hand cricket game {name}!!!')
#     while True:
#         player_odd_even = input("Enter (o) for odd and (e) for even: ").lower()
#         if player_odd_even not in ['o', 'e']:
#             print('Enter only even or odd')
#             continue
#         player_toss_input = input('Enter number (1-6): ')
#         if player_toss_input.isdigit():
#             player_toss_input = int(player_toss_input)
#             if 1 <= player_toss_input <= 6:
#                 computer_toss_input = random.randint(1, 6)
#                 toss(player_toss_input, computer_toss_input, player_odd_even)
#                 break
#             else:
#                 print('Enter a number between 1-6')
#         else:
#             print('Enter a valid number')

# if __name__ == '__main__':
#     main()

import random

def first_inning_player_bat(PLAYER_SCORE, COMPUTER_SCORE):
    while True:
        second_bowl_input = input('Enter your number(2-10): ')
        computer_input_bowl = random.randint(0,10)
        if second_bowl_input.isdigit():
            second_bowl_input = int(second_bowl_input)
            if second_bowl_input >= 0 and second_bowl_input <= 10:
                if second_bowl_input != computer_input_bowl and computer_input_bowl != 0:
                    COMPUTER_SCORE += computer_input_bowl
                    print(f'Computer\'s score is {COMPUTER_SCORE}')
                    if COMPUTER_SCORE > PLAYER_SCORE :
                        print('Cmputer wins by 10 wickets.')
                        break
                elif computer_input_bowl == 0:
                    COMPUTER_SCORE += second_bowl_input
                    print(f'Computer\'s score is {COMPUTER_SCORE}')
                    if COMPUTER_SCORE > PLAYER_SCORE :
                        print('Computer wins by 10 wickets.')
                        break
                else:
                    print(f'You chose {second_bowl_input}')
                    print(f'Computer chose: {computer_input_bowl}')
                    print('Computer is out!!!')
                    print(f'Computer\'s total score is {COMPUTER_SCORE}')
                    if COMPUTER_SCORE < PLAYER_SCORE:
                        print(f'Player wins by {PLAYER_SCORE - COMPUTER_SCORE} runs')
                        break
            else:
                print('Your input should be between 0-10')
        else:
            print('Enter a valid number')

def first_inning_player_bowl(COMPUTER_SCORE,PLAYER_SCORE):
        while True:
            computer_input_bowl = random.randint(0,10)
            score_input = input('Enter your number(1-10): ')
            if score_input.isdigit():
                if int(score_input) >= 0 and int(score_input) <= 10:
                    if int(score_input) != int(computer_input_bowl) and int(score_input) != 0:
                        PLAYER_SCORE += int(score_input)
                        print(f'Your score is {PLAYER_SCORE}')
                        if PLAYER_SCORE > COMPUTER_SCORE:
                            print('You win by 10 wickets!')
                            break
                    elif int(score_input) == 0:
                        PLAYER_SCORE += computer_input_bowl
                        print(f'Your score is {PLAYER_SCORE}')
                        if PLAYER_SCORE > COMPUTER_SCORE:
                            print('You win by 10 wickets!')
                            break
                    else:
                        print(f'You chose {score_input}')
                        print(f'Computer chose: {computer_input_bowl}')
                        print('You are out!!!')
                        print(f'Your total score is {PLAYER_SCORE}')
                        if PLAYER_SCORE < COMPUTER_SCORE:
                            print(f'Computer wins by {COMPUTER_SCORE - PLAYER_SCORE}')
                        break
                else:
                    print('Your input should be between 0-10')
            else:
                print('Enter a valid number')


def first_innings_palyer_toss_win(bat_ball_input):
    PLAYER_SCORE = 0
    COMPUTER_SCORE = 0
    while True:
        computer_input_bowl = random.randint(0,10)
        if bat_ball_input.lower() == 'bat':
            score_input = input('Enter your number(1-10): ')
            if score_input.isdigit():
                if int(score_input) >= 0 and int(score_input) <= 10:
                    if int(score_input) != int(computer_input_bowl) and int(score_input) != 0:
                        PLAYER_SCORE += int(score_input)
                        print(f'Your score is {PLAYER_SCORE}')
                    elif int(score_input) == 0:
                        PLAYER_SCORE += computer_input_bowl
                        print(f'Your score is {PLAYER_SCORE}')
                    else:
                        print(f'You chose {score_input}')
                        print(f'Computer chose: {computer_input_bowl}')
                        print('You are out!!!')
                        print(f'Your total score is {PLAYER_SCORE}')
                        print('')
                        print(f'Computer needs {PLAYER_SCORE} runs to win.')
                        input('Press enter to start bowl')
                        first_inning_player_bat(PLAYER_SCORE, COMPUTER_SCORE)
                        break
                else:
                    print('Your input should be between 0-10')
            else:
                print('Enter a valid number')
        
        elif bat_ball_input.lower() == 'bowl':
            score_input = input('Enter your number(1-10): ')
            if score_input.isdigit():
                if int(score_input) >= 0 and int(score_input) <= 10:
                    if int(score_input) != int(computer_input_bowl) and int(score_input) != 0:
                        COMPUTER_SCORE += computer_input_bowl
                        print(f'Computer\'s score is {COMPUTER_SCORE}')
                    elif int(score_input) == 0:
                        COMPUTER_SCORE += int(score_input)
                        print(f'Computer\'s score is {COMPUTER_SCORE}')
                    else:
                        print(f'You chose {score_input}')
                        print(f'Computer chose: {computer_input_bowl}')
                        print('Computer is out!!!')
                        print(f'Computer\'s total score is {COMPUTER_SCORE}')
                        print('')
                        print(f'You need {COMPUTER_SCORE} runs to win.')
                        input('Press enter to start batting.')
                        first_inning_player_bowl(COMPUTER_SCORE,PLAYER_SCORE)
                        break
                else:
                    print('Your input should be between 0-10')
            else:
                print('Enter a valid number')

def computer_first_bat(COMPUTER_SCORE, PLAYER_SCORE):
    while True:
            computer_input_bowl = random.randint(0,10)
            score_input = input('Enter your number(1-10): ')
            if score_input.isdigit():
                if int(score_input) >= 0 and int(score_input) <= 10:
                    if int(score_input) != int(computer_input_bowl) and int(score_input) != 0:
                        PLAYER_SCORE += int(score_input)
                        print(f'Your score is {PLAYER_SCORE}')
                        if PLAYER_SCORE > COMPUTER_SCORE:
                            print('You win by 10 wickets!')
                            break
                    elif int(score_input) == 0:
                        PLAYER_SCORE += computer_input_bowl
                        print(f'Your score is {PLAYER_SCORE}')
                        if PLAYER_SCORE > COMPUTER_SCORE:
                            print('You win by 10 wickets!')
                            break
                    else:
                        print(f'You chose {score_input}')
                        print(f'Computer chose: {computer_input_bowl}')
                        print('You are out!!!')
                        print(f'Your total score is {PLAYER_SCORE}')
                        if PLAYER_SCORE < COMPUTER_SCORE:
                            print(f'Computer wins by {COMPUTER_SCORE - PLAYER_SCORE}')
                        break
                else:
                    print('Your input should be between 0-10')
            else:
                print('Enter a valid number')

def computer_first_bowl(PLAYER_SCORE, COMPUTER_SCORE):
    while True:
        second_bowl_input = input('Enter your number(2-10): ')
        computer_input_bowl = random.randint(0,10)
        if second_bowl_input.isdigit():
            second_bowl_input = int(second_bowl_input)
            if second_bowl_input >= 0 and second_bowl_input <= 10:
                if second_bowl_input != computer_input_bowl and computer_input_bowl != 0:
                    COMPUTER_SCORE += computer_input_bowl
                    print(f'Computer\'s score is {COMPUTER_SCORE}')
                    if COMPUTER_SCORE > PLAYER_SCORE :
                        print('Cmputer wins by 10 wickets.')
                        break
                elif computer_input_bowl == 0:
                    COMPUTER_SCORE += second_bowl_input
                    print(f'Computer\'s score is {COMPUTER_SCORE}')
                    if COMPUTER_SCORE > PLAYER_SCORE :
                        print('Computer wins by 10 wickets.')
                        break
                else:
                    print(f'You chose {second_bowl_input}')
                    print(f'Computer chose: {computer_input_bowl}')
                    print('Computer is out!!!')
                    print(f'Computer\'s total score is {COMPUTER_SCORE}')
                    if COMPUTER_SCORE < PLAYER_SCORE:
                        print(f'Player wins by {PLAYER_SCORE - COMPUTER_SCORE} runs')
                        break
            else:
                print('Your input should be between 0-10')
        else:
            print('Enter a valid number')


def first_innings_computer_toss_win(Computer_Bat_Ball_Input):
    PLAYER_SCORE = 0
    COMPUTER_SCORE = 0
    while True:
        computer_input_bowl = random.randint(0,10)
        if Computer_Bat_Ball_Input == 'Bat':
            score_input = input('Enter your number(1-10): ')
            if score_input.isdigit():
                if int(score_input) >= 0 and int(score_input) <= 10:
                    if int(score_input) != int(computer_input_bowl) and int(score_input) != 0:
                        COMPUTER_SCORE += computer_input_bowl
                        print(f'Computer\'s score is {COMPUTER_SCORE}')
                    elif int(score_input) == 0:
                        COMPUTER_SCORE += int(score_input)
                        print(f'Computer\'s score is {COMPUTER_SCORE}')
                    else:
                        print(f'You chose {score_input}')
                        print(f'Computer chose: {computer_input_bowl}')
                        print('Computer is out!!!')
                        print(f'Computer\'s total score is {COMPUTER_SCORE}')
                        print(f'You need {COMPUTER_SCORE} runs to win.')
                        input('Press enter to start batting.')
                        computer_first_bat(COMPUTER_SCORE, PLAYER_SCORE)
                        break
                else:
                    print('Your input should be between 0-10')
            else:
                print('Enter a valid number')
        
        elif Computer_Bat_Ball_Input == 'Bowl':
            score_input = input('Enter your number(1-10): ')
            if score_input.isdigit():
                if int(score_input) >= 0 and int(score_input) <= 10:
                    if int(score_input) != int(computer_input_bowl) and int(score_input) != 0:
                        PLAYER_SCORE += int(score_input)
                        print(f'Your score is {PLAYER_SCORE}')
                    elif int(score_input) == 0:
                        PLAYER_SCORE += computer_input_bowl
                        print(f'Your score is {PLAYER_SCORE}')
                    else:
                        print(f'You chose {score_input}')
                        print(f'Computer chose: {computer_input_bowl}')
                        print('You are out!!!')
                        print(f'Your total score is {PLAYER_SCORE}')
                        print(f'Computer needs {PLAYER_SCORE} runs to win.')
                        input('Press enter to start bowling.')
                        computer_first_bowl(PLAYER_SCORE, COMPUTER_SCORE)
                        break
                else:
                    print('Your input should be between 0-10')
            else:
                print('Enter a valid number')


def toss(player_toss_input,computer_toss_input,player_odd_even):
    if player_odd_even.lower() == 'o':
        if (int(player_toss_input) + int(computer_toss_input)) % 2 != 0:
            print(f'Computer input: {computer_toss_input}')
            output = 'Player wins'
        else:
            print(f'Computer input: {computer_toss_input}')
            output = 'Computer wins'
    if player_odd_even.lower() == 'e':
        if (int(player_toss_input) + int(computer_toss_input)) % 2 == 0:
            print(f'Computer input: {computer_toss_input}')
            output = 'Player wins'
        else:
            print(f'Computer input: {computer_toss_input}')
            output = 'Computer wins'
    
    print(output)

    if output.lower() == 'player wins':
        Bat_Ball_Input = input('What do you choose Bat/Bowl: ')
        first_innings_palyer_toss_win(Bat_Ball_Input)
    else:
        Computer_Bat_Ball_Input = random.choice(['Bowl','Bat'])
        print(f'Computer chose to {Computer_Bat_Ball_Input}')
        first_innings_computer_toss_win(Computer_Bat_Ball_Input)


def main():
    name = input('Enter your name: ')
    print(f'Welcome to hand cricket game {name}!!!')
    run = True
    
    while run:
        Player_odd_even = input("Enter (o) for odd and (e) for even: ")
        if Player_odd_even.lower() != 'o' and Player_odd_even.lower() != 'e':
            print('Enter only even or odd')
            continue
        Player_Toss_Input = input('Enter number: ')
        Computer_Toss_Input = random.randint(1,6)
        if Player_Toss_Input.isdigit():
            if int(Player_Toss_Input) < 1 or int(Player_Toss_Input) > 6:
                print('Enter a number between 1-6')
                continue
            else:
                toss(Player_Toss_Input, Computer_Toss_Input,Player_odd_even)
                break
        else:
            print('Enter a valid number')
            continue

        
if __name__ == '__main__':
    main()


