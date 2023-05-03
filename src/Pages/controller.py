import tkinter as tk
from tkinter import *
try:
    import Tkinter as tk
except:
    import tkinter as tk
from Pages.start_page import StartPage as Home
from Pages.directed import Directed

class Controller:
    def __init__(self):
        self.root = tk.Tk()
        self.pages = {}
        self.add_page("Home", Home)
        self.add_page("Directed", Directed)
        self.show_page("Home")
    
    def add_page(self, name, klass):
        self.pages[name] = klass(self.root, self)
    
    def show_page(self, name):
        self.pages[name].tkraise()
    
    def run(self):
        self.root.mainloop()