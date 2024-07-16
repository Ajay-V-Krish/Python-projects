import curses
from curses import wrapper
import time
import random

def display_screen(stdscr):
    stdscr.clear()
    stdscr.addstr('Welcome to the Speed Typing Test!')
    stdscr.addstr('\nPress any key to begin')
    stdscr.refresh()
    stdscr.getkey()

def display_overlay(stdscr, target, current, wpm=0):
    stdscr.addstr(target)
    stdscr.addstr(1, 0, f'WORDS PER MINUTE(WPM): {wpm}')
        
    for i, char in enumerate(current):
        correct_char = target[i]
        color = curses.color_pair(1)
        if char != correct_char:
            color = curses.color_pair(2)
        stdscr.addstr(0, i, char, color)

def load_txt():
    with open('test.txt', 'r') as f:
        lines = f.readlines()
        return random.choice(lines).strip()

def wpm_test(stdscr):
    target_text = load_txt()
    current_text = []
    wpm = 0
    start_time = time.time()
    stdscr.nodelay(True)
    
    while True:
        time_elapsed = time.time() - start_time
        if time_elapsed > 0:
            wpm = round((len(current_text) / (time_elapsed / 60)) / 5)

        stdscr.clear()
        display_overlay(stdscr, target_text, current_text, wpm)
        stdscr.refresh()

        if "".join(current_text) == target_text:
            stdscr.nodelay(False)
            break

        try:
            key = stdscr.getkey()
        except Exception as e:
            continue

        if ord(key) == 27:  # ASCII value for ESC key.
            break
        if key in ("KEY_BACKSPACE", '\b', '\x7f'):  # Name of backspace key in different OS.
            if len(current_text) > 0:
                current_text.pop()
        elif len(current_text) < len(target_text):
            current_text.append(key)

def main(stdscr):
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)

    display_screen(stdscr)
    while True:
        wpm_test(stdscr)
        stdscr.addstr(3,0, "You completed the text!Press any key to continue..../Esc to exit")
        key = stdscr.getkey()
        if ord(key) == 27:
            break


wrapper(main)


#import curses
# from curses import wrapper
# import random
# import time

# def disply_screen(stdscr):
#     stdscr.clear()
#     stdscr.addstr('Welcome to the Speed Typing Test!')
#     stdscr.addstr('\nPress any key to begin')
#     stdscr.refresh()
#     stdscr.getkey()

# def display_overlay(stdscr, target, current, wpm=0):
#     stdscr.addstr(target)
#     stdscr.addstr(1, 0, f'WPM: {wpm}')
        
#     for i,chars in enumerate(current):
#         correct_char = target[i]
#         color = curses.color_pair(1)
#         if chars != correct_char:
#             color = curses.color_pair(2)
#         stdscr.addstr(0, i, chars, color)


# def wpm_test(stdscr):
#     target_text = 'Hello World is the first program for every programmers.'
#     current_text = []
#     wpm = 0
#     start_time = time.time()
#     stdscr.nodelay(True)
    
#     while True:
#         time_elapsed = max(time.time() - start_time, 1)
#         wpm = round((len(current_text) / (time_elapsed / 60))/5)

#         stdscr.clear()
#         display_overlay(stdscr,target_text, current_text)
#         stdscr.refresh()

#         try:
#             key = stdscr.getkey()
#         except:
#             continue

#         if ord(key) == 27:#ASCI value for esc key.
#             break
#         if key in ("KEY_BACKSPACE", '\b', 'x7f'):#name of backspace key in different os. WE HAVE GIVEN FUNCTION TO BACKSPACE
#             if len(current_text) > 0:
#                 current_text.pop()
#         elif len(current_text) < len(target_text):
#             current_text.append(key)

# def main(stdscr):
#     curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
#     curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
#     curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)

#     disply_screen(stdscr)
#     wpm_test(stdscr)

# wrapper(main)
