import random

User_Name = input('Enter your name: ')

print(f'Good Luck {User_Name}')

words = ['cricket', 'rugby', 'hockey', 'football', 'tennis', 'volleyball', 'badminton']

word = random.choice(words)

print('Guess a character in the word: ')

turns = 3

guesses =''

while turns>0:
    wrong_choice = 0
    for char in word:
        if char in guesses:
            print(char, end='')
        else:
            print('_', end='')
            wrong_choice += 1

    if wrong_choice == 0:
        print('You win😊😊😊')
        print(f'The word is {word}')
        break

    guess = input('Guess the character: ')
    guesses += guess
    
    if guess not in word:

        turns -= 1
        print('wrong')
        print(f'You have {turns} more guesses')

    if turns == 0:
        print(f'You lost. The secret word was {word}')