import serial # Import the PySerial library
import threading
import pygame
import time
from gamepad import t_pressed


ser = serial.Serial("/dev/ttyACM1", 9600)
n = str.encode("\n")

# Send character 'S' to start the program

def t_pressed(side, axis):
    while True:
        if pygame.joystick.Joystick(0).get_axis(axis) > 0: #LT
            command = str.encode(side + "\r\n")
            ncommand = str.encode(side + "#")
            ser.write(command)
            ser.write(ncommand)
            print(side, "T", "pressed")
        
        
        
    

t1 = threading.Thread(target=t_pressed, args=("L", 2))
t2 = threading.Thread(target=t_pressed, args=("R", 5))
t1.start()
t2.start()



# Read line   s
while True:
    bs = ser.readline()
    print(bs)