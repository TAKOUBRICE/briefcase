"""
creation des widgets
"""

import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW, BOLD, CENTER, END

#*************************** Container par defaut **************************************
#couler 
col = {

"blue":"#0d6efd", "indigo": "#6610f2", "purple":"#6f42c1", "pink":"#d63384", "red":"#dc3545", "orange":"#fd7e14","yellow":"#ffc107",
"green":"#198754", "teal":"#20c997", "cyan":"#0dcaf0", "black":"#000000","white":"#ffffff", "gray":"#6c757d","gray-dark":"#343a40",
"gray-100":"#f8f9fa","gray-200": "#e9ecef","gray-300":"#dee2e6","gray-400":"#ced4da","gray-500":"#adb5bd","gray-600":"#6c757d","gray-700":"#495057",
"gray-800":"#343a40","gray-900":"#212529","primary":"#0d6efd","secondary":"#6c757d","success":"#198754","info":"#0dcaf0","warning":"#ffc107",
"danger":"#dc3545","light":"#f8f9fa","dark":"#212529","primary-text":"#052c65","secondary-text":"#2b2f32","success-text":"#0a3622",
"info-text":"#055160","warning-text":"#664d03","danger-text":"#58151c","light-text":"#495057","dark-text":"#495057",
"primary-subtle":"#cfe2ff","secondary-subtle":"#e2e3e5","success-subtle":"#d1e7dd","info-subtle":"#cff4fc","warning-subtle":"#fff3cd",
"danger-subtle":"#f8d7da","light-subtle":"#fcfcfd","dark-subtle":"#ced4da","primary-border-subtle":"#9ec5fe","secondary-border-subtle":"#c4c8cb","success-border-subtle":"#a3cfbb",
"info-border-subtle":"#9eeaf9","warning-border-subtle":"#ffe69c","danger-border-subtle":"#f1aeb5","light-border-subtle":"#e9ecef","dark-border-subtle":"#adb5bd"

}
def texte(txt: str, fz: int = 16, cl = col['dark-text']):
    togglelabel = toga.Label(text= txt,style=Pack(font_size=fz, padding= 5, background_color= col['gray-200'], color= cl))
    toggle = toga.Box(style=Pack(direction=ROW, padding=10))
    toggle.add(togglelabel)
    return toggle
class textIcon:
    
    def textSuccess(self):
        icon = texte("✔️", fz= 16, cl=col['success'])
        return icon
    def textDanger(self):
        icon = texte("❌",fz=16, cl=col['danger'])
        return icon
    def textInfo(self):
        icon = texte("ℹ️",fz=16, cl=col['info'])
        return icon
    def textWarning(self):
        icon = texte("⚠️",fz=16, cl=col['warning'])
        return icon
    def textReset(self):
        icon = texte("🔁",fz=16, cl=col['dark'])
        return icon
    def textMark(self):
        icon = texte("🏷️")
        return icon
    def textSearch(self):
        icon = texte("🔍")
        return icon
    def textAdd(self):
        icon = texte("➕")
        return icon
    def textDelete(self):
        icon = texte("🗑️")
        return icon
    def textEdit(self):
        icon = texte("✏️")
        return icon
    def textSave(self):
        icon = texte("💾")
        return icon
    def textUpdate(self):
        icon = texte("🔄")
        return icon
    def textUp(self):
        icon = texte("⬆️")
        return icon
    def textDown(self):
        icon = texte("⬇️")
        return icon
    def textSettings(self):
        icon = texte("⚙️")
        return icon
    def textHome(self):
        icon = texte("🏠")
        return icon
    def textBack(self):
        icon = texte("🔙")
        return icon
    def textLeft(self):
        icon = texte("⬅️")
        return icon
    def textRight(self):
        icon = texte("➡️")
        return icon

#**********************************************************************************
def btn(text: str ,bg, col, on_press=None, fz = 14):
    return toga.Button(
        text=text,
        on_press=on_press,
        style=Pack(
            font_size=fz,
            padding=10,
            background_color=bg,
            color=col
        )
    )
class button:  
    def get_button(self):
        return self.button
    def width(self, w: int):
        self.button.style.update(width=w)
    #heritage de button
class primary(button):
    def __init__(self, app_instance, text: str, on_press=None):
        self.app = app_instance
        self.text = text
        self.on_press = on_press
        self.button = btn(text=self.text,on_press=self.on_press,bg=col['primary'],col=col['light-text'])


class secondary (button):
    def __init__(self, app_instance, text: str, on_press=None):
        self.app = app_instance
        self.text = text
        self.on_press = on_press
        self.button = btn(
            text=self.text,on_press=self.on_press,bg=col['secondary'], col=col['light-text'])
        
class danger (button):
    def __init__(self, app_instance, text: str, on_press=None):
        self.app = app_instance
        self.text = text
        self.on_press = on_press
        self.button = btn(text=self.text,on_press=self.on_press,bg=col['danger'],col=col['light-text'])
        
class success (button):
    def __init__(self, app_instance, text: str, on_press=None):
        self.app = app_instance
        self.text = text
        self.on_press = on_press
        self.button = btn(text=self.text,on_press=self.on_press,bg=col['success'],col=col['light-text'])
        
class info (button):
    def __init__(self, app_instance, text: str, on_press=None):
        self.app = app_instance
        self.text = text
        self.on_press = on_press
        self.button = btn(text=self.text,on_press=self.on_press,bg=col['info'],col=col['light-text'])
        
class info (button):
    def __init__(self, app_instance, text: str, on_press=None):
        self.app = app_instance
        self.text = text
        self.on_press = on_press
        self.button = btn(text=self.text,on_press=self.on_press,bg=col['info'],col=col['light-text'])
        
class light (button):
    def __init__(self, app_instance, text: str, on_press=None):
        self.app = app_instance
        self.text = text
        self.on_press = on_press
        self.button = btn(text=self.text,on_press=self.on_press,bg=col['light'],col=col['dark-text'])
        
class dark (button):
    def __init__(self, app_instance, text: str, on_press=None):
        self.app = app_instance
        self.text = text
        self.on_press = on_press
        self.button = btn(text=self.text,on_press=self.on_press,bg=col['dark'],col=col['light-text'])
        
#***************************************************************************************
def alt(message: str, bg: str, col: str, icon = None):
    main = toga.Box(style=Pack(direction=ROW, padding=10))
    if icon != None:
        main.add(icon)
    
    text = toga.Label(text=f'{message}',style=Pack(color = col, font_size= 16, padding= 10))
    main.add(text)
    
    toggle = textIcon().textDanger()
    toggle.style.update(justify_content=END)
    main.add(toggle)
    
    return main

class alert:
    def get_alert(self):
        return self.alert
    
class alertPrimary (alert):
    def __init__(self, app_instance,message: str):
        self.app = app_instance
        self.alert = alt(message, bg = col['primary'], col = col['primary-text'])
class alertSecondary (alert):
    def __init__(self, app_instance,message: str):
        self.app = app_instance
        self.alert = alt(message, bg = col['secondary'], col = col['secondary-text'])

class alertSuccess (alert):
    def __init__(self, app_instance,message: str):
        self.app = app_instance
        self.alert = alt(message, bg = col['success'], col = col['success-text'], icon= textIcon().textSuccess())

class alertDanger (alert):
    def __init__(self, app_instance,message: str):
        self.app = app_instance
        self.alert = alt(message, bg = col['danger'], col = col['danger-text'], icon= textIcon().textDanger())
class alertInfo (alert):
    def __init__(self, app_instance,message: str):
        self.app = app_instance
        self.alert = alt(message, bg = col['info'], col = col['light-text'], icon= textIcon().textInfo())
class alertWarning (alert):
    def __init__(self, app_instance,message: str):
        self.app = app_instance
        self.alert = alt(message, bg = col['warning'], col = col['warning-text'], icon= textIcon().textWarning())

        
    
    