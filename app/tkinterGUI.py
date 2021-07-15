import sys
import os
import tkinter as tk
from backend.xlsxEditor import XlsxEditor
from backend.autenticador import Autenticador


class GUI():
    def __init__(self):
        self.root = tk.Tk()
        self.root.attributes('-alpha', 0.85)  # Adiciona transparência
        self.root.overrideredirect(1)  # Retira title bar
        self.root.focus_force()
        self.root.bind('<FocusOut>', self.quit)
        self.startLocation()  # Configura posição inicial para inferior direita
        self.xlsx = None
        try:
            self.xlsx = XlsxEditor()
        except RuntimeError:
            pass

        self.instr = tk.Label(self.root, text='Ponto Eletrônico', bg='yellow')
        self.instr.pack(padx=10, pady=10)

        self.user_auth = tk.Button(self.root, text=self.name(),
                                   command=lambda: self.authentication(), bg=self.color())
        self.user_auth.pack(padx=10, pady=10)

        self.button1 = tk.Button(self.root, text='Início do expediente',
                                 command=lambda: self.editExcel('entrada'))
        self.button1.pack(padx=10, pady=10)

        self.button2 = tk.Button(self.root, text='Início do Intervalo', command=lambda: self.editExcel(
            'inicio_intervalo'))
        self.button2.pack(padx=10, pady=10)

        self.button3 = tk.Button(self.root, text='Fim do Intervalo', command=lambda: self.editExcel(
            'fim_intervalo'))
        self.button3.pack(padx=10, pady=10)

        self.button4 = tk.Button(self.root, text='Fim do expediente',
                                 command=lambda: self.editExcel('saida'))
        self.button4.pack(padx=10, pady=10)

        self.textWidget = tk.Text(self.root, width=35, height=1)
        self.textWidget.pack(padx=10, pady=10)

        # self.updateInfo()

        self.root.mainloop()

    def startLocation(self, w=300, h=350):
        # get screen width and height
        ws = self.root.winfo_screenwidth()  # width of the screen
        hs = self.root.winfo_screenheight()  # height of the screen

        # calculate x and y coordinates for the Tk root window
        x = (ws/2) - (w/2)
        y = (hs/2) - (h/2)

        # set the dimensions of the screen
        # and where it is placed
        self.root.geometry('%dx%d+%d+%d' % (w, h, ws-w-75, hs-h-75))

    # Scripts
    def color(self):
        try:
            if self.xlsx.name:
                return "green"
        except:
            return "red"
    def name(self):
        try:
            return self.xlsx.name
        except:
            return "Autentique-se aqui"
    def authentication(self):
        Autenticador()

    def updateInfo(self):
        self.textWidget.replace('1.0', '1.34', self.xlsx.fetchTodaysData())

    def editExcel(self, evento):
        self.xlsx.updateData(evento)
        self.updateInfo()

    def quit(self, event=None):
        self.root.destroy()


if __name__ == "__main__":
    GUI()
