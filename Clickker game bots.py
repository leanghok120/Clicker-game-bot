
import pyautogui
import time
import keyboard
import random
import win32api, win32con

print("Bot: Enabled")
time.sleep(3)
# Bot features functions
def click(x, y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.000001) #This pauses the script for 0.1 seconds
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

while keyboard.is_pressed("q") == False:
    click(805, 487)
    
print("Bot: Disabled")
