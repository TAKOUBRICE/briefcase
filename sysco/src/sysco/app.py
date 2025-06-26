"""
application de gestion des visiteurs
"""

import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW, CENTER
from .gbstyle import bootstyle, col


class HelloWorld(toga.App):
    """ Premier teste de gbstyle """
    def startup(self):
        main_box = toga.Box(direction=COLUMN, style = Pack(background_color= col['gray-200']))
        #class gbstyle
        self.gbstyle = bootstyle(self)
        boxp = toga.Box(direction=ROW, flex = 0, text_align= CENTER, background_color= col['primary-subtle'])
        
        #hr = self.gbstyle.hr()
        h = self.gbstyle.h('Premier teste de gbstyle', nb= 16)
        textPrimaire =  self.gbstyle.textPrimary('couleur primaire')
        
        boxp.add(h)
        boxp.add(textPrimaire)
        # integrer le box principale
        #main_box.add(h)
        main_box.add(boxp)
        #main_box.add(textPrimaire)
        
        
        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box
        self.main_window.show()       

def main():
    return HelloWorld()
