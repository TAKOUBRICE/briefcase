"""
creation des widgets
"""

import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW,BOLD, CENTER

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

        
class bootstyle:  
    def __init__(self, app_instance):
        self.app = app_instance # Permet  d'accéder à l'instance de l'application Toga
        #self.box = toga.Box(direction=ROW, flex = 0)
        self.label_text = toga.Label("texte ici", style = Pack(margin_top= 0, margin_bottom= 1))
    def exception(self, a,b):
        if not isinstance(a, b):
            raise TypeError(f"l'objet {a} doit être de type ({b}).")
    
    
    def h(self, txt_v: str, nb = 14):
        self.exception(txt_v, str)
        self.exception(nb, int)
        #box_ = self.box
        txt=  self.label_text
        
        txt.text = txt_v
        txt.style.update(font_weight = BOLD, font_size= nb)
        # box_ = box_.style.update(text_align= CENTER)
        # box_.add(txt)
        
        return txt
    
    def textPrimary(self, txt_v: str):
        self.exception(txt_v, str)
        
        #box_ = self.box
        txt =  self.label_text
        
        txt.text = txt_v
        txt.style.update(color = col['primary-text'])
        # box_ = box_.style.update(text_align= CENTER, background_color= col['primary-subtle'])
        # box_.add(txt)
        
        return txt
        
        
        
        
              
        