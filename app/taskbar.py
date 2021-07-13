import os
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QSystemTrayIcon, QMenu, QAction
import webbrowser

from .tkinterGUI import GUI
from .setupGUI import SetupApp


class TaskBarApp():
    def __init__(self):
        self.trayApp = QApplication([])
        self.trayApp.setQuitOnLastWindowClosed(False)
        self.guiApp = False
        
        # Adicionando ícone
        icon = QIcon(os.path.join("resources", "ico_abla.png"))
        
        # Adicionando para taskbar
        self.tray = QSystemTrayIcon(parent=self.trayApp)
        self.tray.setIcon(icon)
        self.tray.setVisible(True)
        self.tray.setToolTip('Ponto Eletrônico')
        
        # Criando opções
        self.menu = QMenu()

        # Abrindo app
        abrir = QAction('Abrir GUI')
        self.menu.addAction(abrir)
        abrir.triggered.connect(self.openGUI)

        # Configurando app
        configurar = QAction('Configuração')
        self.menu.addAction(configurar)
        configurar.triggered.connect(self.setupGUI)

        # Abrindo arquivo excel atual
        site = QAction('Abrir sharepoint')
        self.menu.addAction(site)
        # Abre o site no navegador padrão, "new" configura a maneira como será aberto
        # "2" significa em uma nova aba
        site.triggered.connect(self.sharePoint)

        # Finalizando App
        quit = QAction("Sair")
        quit.triggered.connect(self.end)
        self.menu.addAction(quit)
        
        # Adicionando opções ao app na taskbar
        self.tray.setContextMenu(self.menu)


        self.trayApp.exec_()

    # Antes de abrir a GUI verifica as configurações do sistema
    def openGUI(self):
        Setup()
        GUI()
    
    def setupGUI(self):
        Setup()

    # Abre navegador na página dos documentos da empresa
    @staticmethod
    def sharePoint(link='https://snlv.sharepoint.com/:f:/s/SNLV/Enh3zL6wzjtIuTnNidPYakIBFdCr6n3yPNXhYQQaoKWtkQ?e=sIWqnE'):
        webbrowser.open_new_tab(link)

    def end(self):
        self.trayApp.quit()
