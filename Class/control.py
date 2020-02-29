import math


class Control(object):

    def __init__(self, window, R0, R1, A, L, C):
        self.R0 = R0
        self.R1 = R1
        self.A = A
        self.L = L
        self.C = C
        sim = Control.simulation(self, window)

    # ----------- Symulacja  -----------
    def simulation(self, windows):
        self.xy = []
        self.I = []

        if windows.sin != None:
            windows.canvas.delete(windows.sin)
        if windows.var.get() == 0:
            windows.messagebox.showinfo("Info", "Wybież jaki wykres redagować")
        elif windows.var.get() == 1:
            Control.Rezystor(self, windows, False)
        elif windows.var.get() == 2:
            Control.Cewka(self, windows)
        else:
            Control.Kondensator(self, windows)
        windows.sin = windows.canvas.create_line(self.xy, fill='blue')

    # ----------- Pobudzenie sin  -----------
    def pobudzenie(windows, t, sygnal):
        if sygnal == 0:
            windows.messagebox.showinfo("Info", "Wybież jaki wykres redagować")
        elif sygnal == 1:
            return (math.sin(t * 0.0209))
        elif sygnal == 2:
            return (1)
        else:
            if (t / 100) % 2 <= 1:
                return (1)
            else:
                return (-1)

    def Rezystor(self, windows, napiecie):
        for t in range(1000):
            U_we = Control.pobudzenie(windows, t, float(windows.var_1.get())) * self.A
            R = self.R0 + self.R1 * math.exp((-1) * self.A * t)
            I = U_we / R
            self.xy.append(t + 20)
            self.xy.append(I + 320)

    def Cewka(self, windows):
        S = 0
        for t in range(1000):
            U_we = Control.pobudzenie(windows, t, float(windows.var_1.get())) * self.A
            U_2 = Control.pobudzenie(windows, t + 1, float(windows.var_1.get())) * self.A
            S = Control.Integral(self, S, U_we, U_2)
            self.xy.append(t + 20)
            self.xy.append(S + 320)

    def Kondensator(self, windows):
        for t in range(1000):
            U_we = Control.pobudzenie(windows, t, float(windows.var_1.get())) * self.A
            R = self.R0 + self.R1 * math.exp((-1) * self.A * t)
            I = U_we / R
            self.xy.append(t + 20)
            self.xy.append(I + 320)

    # ----------- Całkowanie -----------
    def Integral(self, wartosc, a, b):
        S = a + (b - a) / 2
        return (S)

    # ----------- Czyścienie wykresu -----------
    def clean(self):
        if self.sin != None:
            self.canvas.delete(self.sin)
