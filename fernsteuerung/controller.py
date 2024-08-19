# from os import environ    # Disabled for easier debugging
# environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1' # Hide pygame support prompt

import pygame
def eingabe():
    pygame.init()
    pygame.joystick.init()
    joystick = pygame.joystick.Joystick(0)
    joystick.init()
    while True:
        pygame.event.get()
        x = joystick.get_axis(0)
        y = joystick.get_axis(1)
        print(x, y)