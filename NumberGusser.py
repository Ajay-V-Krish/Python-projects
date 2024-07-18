import random
import sys
import argparse

parser = argparse.ArgumentParser(description= ' It plays a rock/paper/scissor game.')

parser.add_argument('-n','--name',metavar='name',required=True)

args = parser.parse_args()

Name = args.name

def play(name):
    print('')
    User_Input = input(f"{name} Enter the range of numbers to be guessed (For ex: 10,5,6 etc..):")
    print('')

    if User_Input.isdigit():
        User_Input = int(User_Input)

    else:
        print(f"{name} Pleae type a number")
        sys.exit()

    Guesses = 0


    while True:
        random_number = random.randint(0,int(User_Input))
        Guesses += 1
        Player_Guess = input(f"{name} Make a guess:")
        print('')
        
        if Player_Guess.isdigit():
            Player_Guess = int(Player_Guess)

        else:
            print(f"{name} Please type a number")
            continue
        
        if Player_Guess == random_number:
            print("🎉🎉🎉Congrats.You got it!!")
            print('')
            break
        
        else:
            if Player_Guess > random_number:
                print("You are",str(Player_Guess-random_number),"above the number")
            else:
                print("You are",str(random_number-Player_Guess),"below the number")
        
    print("You got it in",str(Guesses),"guesses")
    
if __name__ == '__main__':
    play(Name)