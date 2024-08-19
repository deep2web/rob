# https://docs.python.org/3/library/time.html
# https://www.pygame.org/docs/ref/joystick.html

import pygame
import time
import os
import curses
import threading

# Initialisieren Sie das Fenster
#stdscr = curses.initscr()

pygame.joystick.init()
pygame.joystick.Joystick(0).init

print(pygame.joystick.Joystick(0).get_power_level())
print(pygame.joystick.Joystick(0).get_name())
print(pygame.joystick.Joystick(0).get_numaxes())


"""
while True:
    stdscr.addstr(3, 0, str(pygame.joystick.Joystick(0).get_axis(0)))
    stdscr.addstr(4, 0, str(pygame.joystick.Joystick(0).get_axis(1)))
    stdscr.addstr(5, 0, str(pygame.joystick.Joystick(0).get_axis(2)))
    stdscr.addstr(6, 0, str(pygame.joystick.Joystick(0).get_axis(3)))
    stdscr.addstr(7, 0, str(pygame.joystick.Joystick(0).get_axis(4)))
    stdscr.addstr(8, 0, str(pygame.joystick.Joystick(0).get_axis(5)))
    stdscr.refresh()

curses.endwin()"""
   
    


print(pygame.joystick.Joystick(0).get_numballs())


print(pygame.joystick.get_count())


"""
while True:
    pygame.joystick.Joystick(0).rumble(0.01, 0.01, 1000)

"""

def t_pressed(side, axis):
    while True:
        if pygame.joystick.Joystick(0).get_axis(axis) > 0: #LT
            print(side, "T", "pressed")
            return side
        time.sleep(0.05)

t1 = threading.Thread(target=t_pressed, args=("L", 2))
t2 = threading.Thread(target=t_pressed, args=("R", 5))
t1.start()
t2.start()



"""
LT = "pygame.joystick.Joystick(0).get_axis(2)"
print(pygame.joystick.Joystick(0).get_axis(2))
while True:
    if pygame.joystick.Joystick(0).get_axis(2) > 0: #LT
        print("LT gedrückt")
        time.sleep(0.5)
"""