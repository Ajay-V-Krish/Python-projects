import random

print("Welcome to Random Password Gernerator")

random_characters = "ABCDEFGHIJKLMNOPQSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$&*"

no_input = int(input("Enter the number of passwords to be generated: "))

no_characters = int(input("Enter the number of characters in the password: "))

print("Here are your passwords:")

for i in range(no_input):
    pass_word = ''
    for c in range(no_characters):
        pass_word += random.choice(random_characters)
    print(pass_word)