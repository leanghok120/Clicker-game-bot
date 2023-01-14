import pyautogui
import time
import keyboard

def cords():
    print("Coordinates Gathering: Enabled")
    time.sleep(5)
    for i in range(0, 11):
        print(pyautogui.position())
        i += 1
        time.sleep(0.5)
    print("Coordinates Gathering: Disabled")