from tkinter import *
from Class.function import Gui_Windows

if __name__ == '__main__':
    # Create Window
    root = Tk()

    # Create object
    my_gui = Gui_Windows(root)

    root.mainloop()