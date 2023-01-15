import pyautogui
import time
import customtkinter
import tkinter


def cords():
    print("Coordinates Gathering: Enabled")
    root = customtkinter.CTk()
    root.geometry("500x450")
    root.title("Coordinates Gathering")
    frame_1 = customtkinter.CTkFrame(master=root)
    frame_1.pack(pady=20, padx=60, fill="both", expand=True)
    label_1 = customtkinter.CTkLabel(master=frame_1, justify=tkinter.LEFT, text="Coordinates")
    label_1.pack(pady=10, padx=10)

    time.sleep(3)
    for i in range(0, 11):
        label_2 = customtkinter.CTkLabel(master=frame_1, justify=tkinter.LEFT, text=pyautogui.position())
        label_2.pack(pady=10, padx=10)
        time.sleep(0.5)
    root.mainloop()
    print("Coordinates Gathering: Disabled")


cords()
