from tkinter import Tk
from keyboard import add_hotkey
import ctypes

root = Tk()

root.config(bg="black")
root.attributes('-fullscreen', True)
root.attributes('-topmost', True)
#root.wm_attributes("-toolwindow", True)
root.config(cursor="none")
add_hotkey("win+shift+s",root.destroy)  

    
root.mainloop()


