from threading import Thread
from fernsteuerung import controller
from bts7960 import bts7960


def fernsteuerung():
    while True:
        if controller.eingabe == "LR":
            print("Vorwärts")
            bts7960.right



t_controller = Thread(target=fernsteuerung) # Kann erst später implenmentiert weden da der Code auf dem PC Zuhause ist...

t_controller.run()




