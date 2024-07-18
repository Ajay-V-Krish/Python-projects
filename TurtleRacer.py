import turtle
import time
import random

WIDTH, HEIGHT = 500, 500

COLORS = ['red', 'green', 'blue', 'orange', 'yellow', 'violet', 'pink', 'purple', 'black', 'brown']

def racer_input():
    racer = 0
    while True:
        racer = input("Enter the number of turtles to race (2-10): ")
        if racer.isdigit():
            racer = int(racer)
        else:
            print("Input is not numeric...Try again!")
            continue

        if 2 <= racer <=10:
            return racer
        else:
            print('Input is not in range (2-10)....Try again!')
            continue

def race(colors):
    turtles = create_turtles(colors)
    
    while True:
        for racer in turtles:
            distance = random.randint(1, 20)
            racer.forward(distance)

            x, y = racer.pos()
            if y >= HEIGHT // 2 - 10:
                return colors[turtles.index(racer)]

def create_turtles(colors):
    turles = []
    spacingx = WIDTH // (len(colors) + 1)
    for i, color in enumerate(colors):
        racer = turtle.Turtle()
        racer.color(color)
        racer.shape('turtle')
        racer.left(90)
        racer.penup()
        racer.setpos(-WIDTH//2 + (i+1) * spacingx, -HEIGHT//2 + 20)
        racer.pendown()
        turles.append(racer)

    return turles

def init_turtle():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.title('Turtle Racing')


racers = racer_input()
init_turtle()
random.shuffle(COLORS)

colors = COLORS[:racers]

winner = race(colors)
print(f'The winner is turtle with the color {winner}')
