
import pyautogui
import time
import keyboard
import random
import win32api, win32con

print("Bot: Enabled")
# Waits 3 seconds before enabling the bot
time.sleep(3)
# Bot features functions

def auto_click(x, y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.000001) #This pauses the script for 0.1 seconds
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
def auto_upgrade(x, y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.000001) #This pauses the script for 0.1 seconds
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
def auto_upgrade2(x, y): # This function has to be named differently from the first function
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.000001) #This pauses the script for 0.1 seconds
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

while keyboard.is_pressed("q") == False:
    auto_click(x=805, y=487) # Change the x and y coordinates to the coordinates of the object you want to click
    if keyboard.is_pressed("c"):
        auto_upgrade(x=356, y=360)
    if keyboard.is_pressed("x"):
        auto_upgrade2(x=333, y=442)
print("Bot: Disabled")
