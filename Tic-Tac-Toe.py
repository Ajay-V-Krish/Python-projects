INSTRUCTIONS = '''
This will be our Tic-Tac-Toe board.

 1 | 2 | 3 
---|---|---
 4 | 5 | 6  
---|---|---
 7 | 8 | 9 

 *instructions:
 1. Insert the spot number(1-9) to put your sign.
 2. You must fill all 9 spots to get result.
 3. Player 1 will start first.
    
'''
sign_list = []
for i in range(9):
    sign_list.append(' ')

def print_board():

    board = f'''
    {sign_list[0]} | {sign_list[1]} | {sign_list[2]} 
   ---|---|---
    {sign_list[3]} | {sign_list[4]} | {sign_list[5]}  
   ---|---|---
    {sign_list[6]} | {sign_list[7]} | {sign_list[8]}
'''
    
    print(board)

index_list = []
def take_input(player_name):
    while True:
        x = int(input(f'{player_name}: '))
        x -= 1
        if 0 <= x < 10:
            if x in index_list:
                print('This spot is blocked')
                continue
            index_list.append(x)
            return x
        print("Please enter a number between 1-9")

def calculate_response(player_one, player_two):
    if (sign_list[0] == sign_list[1] == sign_list[2] == 'X' or
        sign_list[3] == sign_list[4] == sign_list[5] == 'X' or
        sign_list[6] == sign_list[7] == sign_list[8] == 'X' or
        sign_list[0] == sign_list[3] == sign_list[6] == 'X' or
        sign_list[1] == sign_list[4] == sign_list[7] == 'X' or
        sign_list[2] == sign_list[5] == sign_list[8] == 'X' or
        sign_list[0] == sign_list[4] == sign_list[8] == 'X' or
        sign_list[2] == sign_list[4] == sign_list[6] == 'X'):
        print(f"Congratulations. {player_one}. You won it!!!")
        quit("Thank you both for joining")
    elif (sign_list[0] == sign_list[1] == sign_list[2] == 'O' or
          sign_list[3] == sign_list[4] == sign_list[5] == 'O' or
          sign_list[6] == sign_list[7] == sign_list[8] == 'O' or
          sign_list[0] == sign_list[3] == sign_list[6] == 'O' or
          sign_list[1] == sign_list[4] == sign_list[7] == 'O' or
          sign_list[2] == sign_list[5] == sign_list[8] == 'O' or
          sign_list[0] == sign_list[4] == sign_list[8] == 'O' or
          sign_list[2] == sign_list[4] == sign_list[6] == 'O'):
        print(f"Congratulations. {player_two}. You won it!!!")
        quit("Thank you both for joining")

def main():
    print('')
    print("Welcome to Tic-Tac-Toe game")
    print('')
    player_one = input("Enter your name (Player-1): ")
    player_two = input('Enter your name (player-2): ')
    print('')
    print(f'Welcome to the game {player_one} and {player_two}.')

    print(INSTRUCTIONS)
    print(f'{player_one}\'s sign will be (X)')
    print(f'{player_two}\'s sign will be (O)')
    input('Press any key to start the game.')
    
    print_board()

    for i in range(9):
        if i % 2 == 0:
            index = take_input(player_one)
            sign_list[index] = 'X'
        else:
            index = take_input(player_two)
            sign_list[index] = 'O'
            
        print_board()
        calculate_response(player_one,player_two)

    print('This is a tie game. Play again')

main()