import sys
import os
import tkinter as tk
from backend.xlsxEditor import XlsxEditor


class GUI():
    def __init__(self):
        self.root = tk.Tk()
        self.root.attributes('-alpha',0.85) # Adiciona transparência
        self.root.overrideredirect(1) # Retira title bar
        self.root.focus_force()
        self.root.bind('<FocusOut>', self.quit)
        self.startLocation() # Configura posição inicial para inferior direita

        # self.canvas = tk.Canvas(self.root, width=300, height=435)
        # self.canvas.grid(columnspan=1, rowspan=3)
        # self.canvas.bind('<FocusOut>', self.quit)

        self.xlsx = XlsxEditor(f"C:\\Users\\{os.getlogin()}\\SNLV\\SNLV - Documentos\\Ponto Eletronico\\Banco_de_Horas.xlsx")

        funcionarios = self.xlsx.wb.sheetnames

        value_inside = tk.StringVar(self.root)
        value_inside.set("Seu nome")
        question_menu = tk.OptionMenu(self.root, value_inside, *funcionarios)
        question_menu.pack(padx=10, pady=10)

        self.instr = tk.Label(self.root, text='Ponto Eletrônico', bg='yellow')
        self.instr.pack(padx=10, pady=10)

        self.button1 = tk.Button(self.root, text='Início do expediente', command=lambda: self.editExcel(value_inside.get(), 'entrada'))
        self.button1.pack(padx=10, pady=10)

        self.button2 = tk.Button(self.root, text='Início do Intervalo', command=lambda: self.editExcel(value_inside.get(), 'inicio_intervalo'))
        self.button2.pack(padx=10, pady=10)

        self.button3 = tk.Button(self.root, text='Fim do Intervalo', command=lambda: self.editExcel(value_inside.get(), 'fim_intervalo'))
        self.button3.pack(padx=10, pady=10)

        self.button4 = tk.Button(self.root, text='Fim do expediente', command=lambda: self.editExcel(value_inside.get(), 'saida'))
        self.button4.pack(padx=10, pady=10)

        self.textWidget = tk.Text(self.root, width=35, height=1)
        self.textWidget.pack(padx=10, pady=10)

        self.root.mainloop()

    def startLocation(self, w=300, h=350):
        # get screen width and height
        ws = self.root.winfo_screenwidth() # width of the screen
        hs = self.root.winfo_screenheight() # height of the screen

        # calculate x and y coordinates for the Tk root window
        x = (ws/2) - (w/2)
        y = (hs/2) - (h/2)

        # set the dimensions of the screen 
        # and where it is placed
        self.root.geometry('%dx%d+%d+%d' % (w, h, ws-w-75, hs-h-75))


    # Scripts
    def showInfo(self, dados_de_hoje):
        self.textWidget.replace('1.0', '1.34', dados_de_hoje)

    def editExcel(self, nome, evento):
        if nome != 'Seu nome':
            atual = self.xlsx.insertData(nome, evento)
            self.showInfo(' -- '.join(list(filter(None, atual))))
        else:
            self.showInfo('Favor selecionar nome')

    def quit(self, event=None):
        self.root.destroy()


if __name__ == "__main__":
    # Roda configurações se não tiver rodado ainda
    GUI()