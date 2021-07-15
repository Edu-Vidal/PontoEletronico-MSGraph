import sys
import os
import tkinter as tk


class GUI():
    def __init__(self, manager):
        self.root = tk.Tk()
        self.root.attributes('-alpha', 0.85)  # Adiciona transparência
        self.root.overrideredirect(1)  # Retira title bar
        self.root.focus_force()
        self.root.bind('<FocusOut>', self.quit)
        self.startLocation()  # Configura posição inicial para inferior direita

        self.manager = manager

        self.instr = tk.Label(self.root, text='Ponto Eletrônico', bg='yellow')
        self.instr.pack(padx=10, pady=10)

        self.user_auth = tk.Button(
            self.root,
            text=self.manager.name if self.manager.autenticado else "Autentique-se aqui",
            command=self.manager.authenticate,
            bg='green' if self.manager.autenticado else "red"
        )
        self.user_auth.pack(padx=10, pady=10)

        self.button1 = tk.Button(self.root, text='Início do expediente',
                                 command=lambda: self.editExcel('entrada'))
        self.button1.pack(padx=10, pady=10)

        self.button2 = tk.Button(self.root, text='Início do Intervalo',
                                command=lambda: self.editExcel('inicio_intervalo'))
        self.button2.pack(padx=10, pady=10)

        self.button3 = tk.Button(self.root, text='Fim do Intervalo',
                                command=lambda: self.editExcel('fim_intervalo'))
        self.button3.pack(padx=10, pady=10)

        self.button4 = tk.Button(self.root, text='Fim do expediente',
                                 command=lambda: self.editExcel('saida'))
        self.button4.pack(padx=10, pady=10)

        self.textWidget = tk.Text(self.root, width=35, height=1)
        self.textWidget.pack(padx=10, pady=10)

        self.textWidget.replace('1.0', '1.34', self.manager.excel.todaysData)

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
    def updateInfo(self):
        if self.manager.autenticado:
            self.manager.excel.fetchTodaysData()
        else:
            self.textWidget.replace('1.0', '1.34', 'Autentique-se')

    def editExcel(self, evento):
        if self.manager.autenticado:
            self.manager.excel.updateData(evento)
            self.updateInfo()
        else:
            self.textWidget.replace('1.0', '1.34', 'Autentique-se')

    def quit(self, event=None):
        self.root.destroy()


if __name__ == "__main__":
    GUI()
