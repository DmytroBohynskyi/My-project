from tkinter import *
from Class.control import Control

#Static file
IMAGE_STATIC = "Image/"

class Gui_Windows(object):
    def __init__(self, master):
        master.title("Symulacja obwodu RLC")
        master.geometry('1320x640')
        master.resizable(False, False)

        self.canvas = Canvas(master, width=1040, height=640, bg='#002')
        self.canvas.pack(side='right')

        self.sin = None

        # ----------- Wertykalna linia -----------
        for y in range(21):
            k = 50 * y
            self.canvas.create_line(20 + k, 620, 20 + k, 20, width=1, fill='#191936')

        # ----------- Horyzontalna linia -----------
        for x in range(13):
            k = 50 * x
            self.canvas.create_line(20, 20 + k, 1020, 20 + k, width=1, fill='#191936')

        # ----------- Oś X i Y -----------
        self.canvas.create_line(20, 20, 20, 620, width=1, arrow=FIRST, fill='white')  # To Y
        self.canvas.create_line(10, 320, 1020, 320, width=1, arrow=LAST, fill='white')  # To X

        self.canvas.create_text(20, 10, text="300 [I]", fill='white')
        self.canvas.create_text(20, 630, text="-300 [I]", fill='white')
        self.canvas.create_text(10, 310, text="0", fill='white')
        self.canvas.create_text(1030, 310, text="1000", fill='white')

        # ----------- Definiujemy napisy -----------
        self.label_A = Label(master, text="Amplituda")
        self.label_A.place(x=0, y=10)
        self.label_R0 = Label(master, text='Wartość Ro')
        self.label_R0.place(x=0, y=30)
        self.label_R1 = Label(master, text="Wartość R1:")
        self.label_R1.place(x=0, y=50)
        self.label_L = Label(master, text="Wartość Cewki:")
        self.label_L.place(x=0, y=70)
        self.label_C = Label(master, text="Wartość Kondensatora:")
        self.label_C.place(x=0, y=90)

        # ----------- Definiujemy listbox -----------
        entry_A = Entry(master)
        entry_A.place(x=130, y=10)
        entry_R0 = Entry(master)
        entry_R0.place(x=130, y=30)
        entry_R1 = Entry(master)
        entry_R1.place(x=130, y=50)
        entry_L = Entry(master)
        entry_L.place(x=130, y=70)
        entry_C = Entry(master)
        entry_C.place(x=130, y=90)

        # ----------- Definiujemy Radio Buttons -----------
        self.var = IntVar()
        self.rbutton1 = Radiobutton(master, text='Opornik', variable=self.var, value=1)
        self.rbutton2 = Radiobutton(master, text='Induktor', variable=self.var, value=2)
        self.rbutton3 = Radiobutton(master, text='Kondensator', variable=self.var, value=3)
        self.rbutton1.place(x=10, y=150)
        self.rbutton2.place(x=10, y=170)
        self.rbutton3.place(x=10, y=190)

        # ----------- Dodajemy zdjęcie do programu -----------
        self.photo = PhotoImage(file="{}/RLC.png".format(IMAGE_STATIC))
        self.label_photo = Label(master, image=self.photo)
        self.label_photo.pack(side=BOTTOM)

        # ----------- Definiujemy Radio Buttons -----------
        self.var_1 = IntVar()
        self.rbutton4 = Radiobutton(master, text='Sinusoida', variable=self.var_1, value=1)
        self.rbutton5 = Radiobutton(master, text='Skok ', variable=self.var_1, value=2)
        self.rbutton6 = Radiobutton(master, text='Fala prostokątna', variable=self.var_1, value=3)
        self.rbutton4.place(x=140, y=150)
        self.rbutton5.place(x=140, y=170)
        self.rbutton6.place(x=140, y=190)

        btn_cols = Button(master, text="Symulacja")
        btn_cols.bind('<Button-1>', lambda event: Control(self, float(entry_R0.get()), float(entry_R1.get()),
                                                          float(entry_A.get()), float(entry_L.get()),
                                                          float(entry_C.get())))
        btn_cols.place(x=10, y=240, height=50, width=120)

        btn_clean = Button(master, text="Wyciść")
        btn_clean.bind('<Button-1>', lambda event: Control.clean(self))
        btn_clean.place(x=140, y=240, height=50, width=120)

        btn_cols = Button(master, text="AUTO")
        btn_cols.bind('<Button-1>',
                      lambda event: Control(self, float(3.34), float(1), float(200), float(0.0229),
                                            float(0.0229)))
        btn_cols.place(x=10, y=300, height=50, width=120)
