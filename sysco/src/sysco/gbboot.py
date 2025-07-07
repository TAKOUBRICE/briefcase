"""
creation des widgets
"""

import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW, BOLD, CENTER
from .gbstyle import bootstyle, col


#******************************************************
# ---------------- outils par defaut ---------------
# ****************************************************
def hr():
    return toga.Box(direction=COLUMN, style = Pack(flex = 1, text_align= CENTER, background_color= "#373738",height=2,margin=(2,0)))
#BOX
def div_c():
    return toga.Box(direction=COLUMN, style = Pack(flex = 1, text_align= CENTER, padding= 10, background_color=col['gray-200']))
def div_r():
    return toga.Box(direction=ROW, style = Pack(flex = 1, text_align= CENTER, padding= 10, background_color=col['gray-200']))
def div_option(box1, box2):
    container = toga.OptionContainer(content=[toga.OptionItem("option1", box1), toga.OptionItem("option2", box2)])
    return container

    

def div_darck(tl = "titre" , content = "contenus du bloc"):
        inner_box = toga.Box(style=Pack(direction=COLUMN, padding=10, background_color='black'))
        # Titre
        title = toga.Label(tl,style=Pack(font_size=20, font_weight='bold', color='white', padding_bottom=10))
        paragraph = toga.Label(content,style=Pack(font_size=10, color='white'))
        # Ajout des éléments dans la hiérarchie
        inner_box.add(title)
        inner_box.add(paragraph)
        return inner_box
def div_light(tl = "titre" , content = "contenus du bloc"):
        inner_box = div()
        # Titre
        title = toga.Label(tl,style=Pack(font_size=20, font_weight='bold', color="#222020", padding_bottom=10))
        paragraph = toga.Label(content,style=Pack(font_size=10, color="#222020"))
        # Ajout des éléments dans la hiérarchie
        inner_box.add(title)
        inner_box.add(paragraph)
        return inner_box
def img (path: str, width=200, height=200):
    image = toga.ImageView(toga.Image(path), style=Pack(width, height,padding=10))
    return image
    
def h1 (text):
    return toga.Label(text, style = Pack(margin_top= 0, margin_bottom= 1,font_size= 40))
def h2 (text):
    return toga.Label(text, style = Pack(margin_top= 0, margin_bottom= 1,font_size= 32))
def h3 (text):
    return toga.Label(text, style = Pack(margin_top= 0, margin_bottom= 1,font_size= 28))
def h4 (text):
    return toga.Label(text, style = Pack(margin_top= 0, margin_bottom= 1,font_size= 24))
def h5 (text):
    return toga.Label(text, style = Pack(margin_top= 0, margin_bottom= 1,font_size= 20))
def h6 (text):
    return toga.Label(text, style = Pack(margin_top= 0, margin_bottom= 1,font_size= 16))



box =  toga.Box(direction=ROW, flex = 0)       