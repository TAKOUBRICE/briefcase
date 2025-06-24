"""
application de gestion des visiteurs
"""

import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW


class HelloWorld(toga.App):
    def say_hello(self, widget):
            print(f"Hello, {self.name_input.value}")
    def startup(self):
        """Construct and show the Toga application.

        Usually, you would add your application to a main content box.
        We then create a main window (with a name matching the app), and
        show the main window.
        """
        main_box = toga.Box(direction=COLUMN)
        # label: pour afficher un texte
        name_label = toga.Label("Your name: ",margin=(0, 5), )
        # text input: pour saisir du texte
        # flex=1: pour que le champ prenne tout l'espace disponible
        self.name_input = toga.TextInput(flex=1)
        name_box = toga.Box(direction=ROW, margin=5)
        name_box.add(name_label)
        name_box.add(self.name_input)
        
        button = toga.Button("Say Hello!", on_press= self.say_hello, margin=5,)
        main_box.add(name_box)
        main_box.add(button)

        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box
        self.main_window.show()

        

def main():
    return HelloWorld()
