import RockPaperScissor
import NumberGusser
import sys
import argparse

parser = argparse.ArgumentParser(description= ' It plays a rock/paper/scissor game.')

parser.add_argument('-n','--name',metavar='name',required=True)

args = parser.parse_args()

Name = args.name

def main(Name):
    
    while True:
        print('')
        print(f"Welcome to the Arcade of games {Name}!")
        print('')

        print('Please choose a game:')
        print('1 = Rock Paper Scissors')
        print('2 = Guess My Number')
        print('')
        print('Press x to exit\n')
        print('')
        
        User_Input = input()
        while True:
            if User_Input == '1':
                RockPaperScissor.rps(Name)
                next_input = input("Press 'y' to continue and 'x' to exit: ")
                if next_input.lower() == 'y':
                    continue
                else:
                    print("🎉🎉🎉Thanks for playing")
                    break
            elif User_Input == '2':
                NumberGusser.play(Name)
                next_input = input("Press 'y' to continue and 'x' to exit: ")
                if next_input.lower() == 'y':
                    continue
                else:
                    print("🎉🎉🎉Thanks for playing")
                    break
            elif User_Input.lower() == 'x':
                sys.exit(f'Bye {Name}')
            else:
                print("Invalid input. Please enter '1', '2', or 'x'.")
        
if __name__ == '__main__':
    main(Name)