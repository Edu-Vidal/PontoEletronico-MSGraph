import sys, os
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QFileDialog
from PyQt5.uic import loadUi

from backend.setup import SetupConfig

# Setup GUI 
class SetupApp():
    def __init__(self, configFile='config.ini'):
        pass


# class FileBrowser(QDialog):
#     def __init__(self):
#         super(FileBrowser,self).__init__()
#         loadUi("gui.ui",self)
#         self.browse.clicked.connect(self.browsefiles)


#     def browsefiles(self):
#         fname=QFileDialog.getOpenFileName(self, 'Open file', f'C:\\Users\\{os.getlogin()}\\SNLV\\SNLV - Documentos', 'Planilha do Microsoft Excel (*.xlsx)')
#         self.filename.setText(fname[0])


# app=QApplication(sys.argv)
# FileBrowser=FileBrowser()
# widget=QtWidgets.QStackedWidget()
# widget.addWidget(FileBrowser)
# widget.setFixedWidth(400)
# widget.setFixedHeight(300)
# widget.show()
# sys.exit(app.exec_())