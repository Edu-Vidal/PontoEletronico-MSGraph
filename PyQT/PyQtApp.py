import os
import sys
from PyQt5.QtGui import QIcon, QGuiApplication
from PyQt5.QtQml import QQmlApplicationEngine
from PyQt5.QtWidgets import QApplication, QSystemTrayIcon, QMenu, QAction
import webbrowser


class PyQtApp():
    def __init__(self):
        app = QGuiApplication(sys.argv)
        engine = QQmlApplicationEngine()
        engine.quit.connect(app.quit)
        engine.load('./app/main.qml')
        sys.exit(app.exec())


if __name__ == "__main__":
    PyQtApp()
    