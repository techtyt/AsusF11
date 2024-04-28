import tkinter as tk
import pyautogui
import keyboard


global root
pyautogui.moveTo(2900, None)
root = tk.Tk()
keyboard.add_hotkey("win+shift+s",root.destroy,print("press"),root.quit)  

root.config(bg="black")
root.attributes('-fullscreen', True)
root.attributes('-topmost', True)
root.mainloop()

    

