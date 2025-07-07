"""
application de gestion des visiteurs
"""

import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW, CENTER
from toga.constants import Direction
#from .gbboot import *
from .gbstyle import *



class HelloWorld(toga.App):
    """ Premier teste de gbstyle """
    def startup(self):
        main_box = toga.Box(style=Pack(direction=COLUMN, padding=20, alignment=CENTER,flex=1, background_color=col['gray-200']))

        # teste des alert
        primary = alertPrimary(self, 'Ceci est un message d\'alerte primaire')
        secondary = alertSecondary(self, 'Ceci est un message d\'alerte secondaire')
        danger = alertDanger(self, 'Ceci est un message d\'alerte danger')
        success = alertSuccess(self, 'Ceci est un message d\'alerte succès')
        info = alertInfo(self, 'Ceci est un message d\'alert info')
        Warning = alertWarning(self, 'Ceci est un message d\'alert Warning')
        
        main_box.add(primary.get_alert())
        main_box.add(secondary.get_alert())
        main_box.add(danger.get_alert())
        main_box.add(success.get_alert())
        main_box.add(info.get_alert())
        main_box.add(Warning.get_alert())
        container = toga.ScrollContainer(content=main_box)
        # Crée la fenêtre principale
        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = container
        self.main_window.show()      

def main():
    return HelloWorld()
