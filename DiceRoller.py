import random

#print("\u25CF \u250C \u2500 \u2510 \u2502 \u2514 \u2518")

# ● ┌ ─ ┐ │ └ ┘

Dice_Drawing = {
    1 : ("┌─────────┐",
         "│         │",
         "│    ●    │",
         "│         │",
         "└─────────┘"),
    2 : ("┌─────────┐",
         "│ ●       │",
         "│         │",
         "│       ● │",
         "└─────────┘"),
    3 : ("┌─────────┐",
         "│ ●       │",
         "│    ●    │",
         "│       ● │",
         "└─────────┘"),
    4 : ("┌─────────┐",
         "│ ●     ● │",
         "│         │",
         "│ ●     ● │",
         "└─────────┘"),
    5 : ("┌─────────┐",
         "│ ●     ● │",
         "│    ●    │",
         "│ ●     ● │",
         "└─────────┘"),
    6 : ("┌─────────┐",
         "│ ●    ●  │",
         "│ ●    ●  │",
         "│ ●    ●  │",
         "└─────────┘")
}

dice = []
total = 0
num_of_dice = input("How mane Dice?  ")

for die in range(int(num_of_dice)):
    dice.append(random.randint(1, 6))

# for die in range(int(num_of_dice)):
#     for line in Dice_Drawing.get(dice[die]):
#         print(line)

for line in range(5):
    for die in dice:
        print(Dice_Drawing.get(die)[line], end='')
    print()

for die in dice:
    total += die
print(f"Total: {total}")