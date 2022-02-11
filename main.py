import random
import time
from math import sin, cos
import keyboard
import pyautogui


class Clicker:
    theta = 0
    step = 1
    h = int(1920/2)
    k = int(1080/2)

    r = 50

    running = True

    @staticmethod
    def run():
        while Clicker.running:
            sleep_time = random.uniform(0, 1)

            x = Clicker.h + Clicker.r*cos(Clicker.theta)
            y = Clicker.k + Clicker.r*sin(Clicker.theta)

            print(f"{x}, {y}")

            if Clicker.theta == 360:
                Clicker.theta = 0

            pyautogui.moveTo(x, y)
            pyautogui.click(x, y)

            Clicker.theta+=Clicker.step

            if keyboard.is_pressed("h"):
                Clicker.running = not Clicker.running
        

Clicker.run()