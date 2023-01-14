import time
import keyboard
import win32api, win32con
import customtkinter
import mouse_pos_gathering

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

root = customtkinter.CTk()
root.geometry("600x550")
root.title("Clicker Game Bot")


# Bot Features
# Click
def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.000001)  # This pauses the script for 0.1 seconds
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)


# Autoclick
def auto_click(x=805, y=487):  # The first argument is the x position and the second is the y position
    while keyboard.is_pressed("q") == False:
        click(x, y)


# Auto upgrade function
class AutoUpgrade1:
    def auto_upgrade_x1(x=330, y=432):
        click(x, y)

    def auto_upgrade_x10(x=330, y=432):
        for i in range(0, 11):
            click(x, y)
            i += 1

    def auto_upgrade_x100(x=330, y=432):
        for i in range(0, 101):
            click(x, y)
            i += 1


# Get cordinates function
def get_cordinates():
    mouse_pos_gathering.cords()


# Frame
frame_1 = customtkinter.CTkFrame(master=root)
frame_1.pack(pady=20, padx=60, fill="both", expand=True)

# Buttons
autoclicker_button = customtkinter.CTkButton(master=frame_1, text="Auto Clicker", command=auto_click)
autoclicker_button.pack(pady=10, padx=10)
autoupgrade_button = customtkinter.CTkButton(master=frame_1, text="Auto Upgrade X1",
                                             command=AutoUpgrade1.auto_upgrade_x1)
autoupgrade_button.pack(pady=10, padx=10)
autoupgrade_x10_button = customtkinter.CTkButton(master=frame_1, text="Auto Upgrade X10",
                                                 command=AutoUpgrade1.auto_upgrade_x10)
autoupgrade_x10_button.pack(pady=10, padx=10)
autoupgrade_x100_button = customtkinter.CTkButton(master=frame_1, text="Auto Upgrade X100",
                                                  command=AutoUpgrade1.auto_upgrade_x100)
autoupgrade_x100_button.pack(pady=10, padx=10)
get_cords_button = customtkinter.CTkButton(master=frame_1, text="Get Cordinates", command=get_cordinates)
get_cords_button.pack(pady=10, padx=10)

if __name__ == "__main__":
    root.mainloop()
