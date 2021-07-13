import os
import configparser
import webbrowser
from PyQt5.QtWidgets import QFileDialog


# Procura um arquivo de configuração para o app principal
# Checa as informações presentes e realiza alterações caso necessário
class SetupConfig():
    def __init__(self, configFile='config.ini'):
        self.configFile = configFile
        self.config = configparser.ConfigParser()


    def setConfig(self, alterar=False):
        # Confirma se o arquivo existe
        if not os.path.exists(self.configFile) and alterar==False:
            self.config['OneDriveConnected'] = self.setOneDrive()
            self.config['SharePointExcelFile'] = self.setSharePointFolderLocation()
            self.config['WindowsStartup'] = self.setWindowsStartup()
            self.config['EmployeeName'] = ''
            # Cria arquivo com configurações estabelecidas acima
            with open(self.configFile, 'w') as f:
                self.config.write(f)
        # Confirma se o arquivo existente está configurado corretamente
        else:
            self.config.read(self.configFile)
            if self.config['OneDriveConnected'] != 1:
                pass
            if not os.path.exists(self.config['SharePointExcelFile']):
                pass

    def setOneDrive(self):
        # Faz login com sua conta vinculada à empresa
        webbrowser.open_new_tab('https://onedrive.live.com/about/pt-br/signin/')

        if "botao apertado":
            return '1'

    def setSharePointFolderLocation(self, docWebsite='https://snlv.sharepoint.com/sites/SNLV/Shared%20Documents/Forms/AllItems.aspx'):
        # Cria pasta local dos arquivos da empresa no Sharepoint

        # Selecione sincronizar e aguarde a configuração
        webbrowser.open_new_tab(docWebsite)

        return self.browseFiles()
    
    def browseFiles(self, startPath=f"C:\\Users\\{os.getlogin()}\\SNLV\\SNLV - Documentos"):
        return QFileDialog.getOpenFileName(
            self, 
            'Open file', 
            self.config['SharePointExcelFile'],
            'Planilha do Microsoft Excel (*.xlsx)')

    def setWindowsStartup(self, state):
        # Configura executável para iniciar junto ao Windows
        pass

    def setEmployeeName(self, name):
        # A partir do instante que o usuário insere seu nome
        # a informação é salva
        pass


if __name__ == "__main__":
    SetupConfig()

