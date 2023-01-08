import pyautogui
import time
import keyboard


print("Coordinates Gathering: Enabled")
time.sleep(5)
while keyboard.is_pressed("q") == False:
    print(pyautogui.position())
    time.sleep(1)
print("Coordinates Gathering: Disabled")