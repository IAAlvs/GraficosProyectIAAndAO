import tkinter as tk
from tkinter import *
try:
    import Tkinter as tk
except:
    import tkinter as tk
from Pages.directed import Directed
from Pages.no_directed import NoDirected
#Start page
class StartPage(tk.Frame):
    def __init__(self, master):#Constructor
        tk.Frame.__init__(self, master)
        #tk.Frame.grid(self,row=0, column=0, sticky='nsew')
        tk.Frame.configure(self,bg="#A8C3B7", width=100)
        tk.Label(self, text="""
        Teoria de graficas:
        Alvarado Sanchez Isaac Alfredo
        Martinez Alan Octavio
        Elige la gráfica la cual quieres realizar
        """, font=('San Francisco', 16),width=50,height=6,bg="#A8C3B7").pack(side="top", fill="x", pady=5)
        #Dirigida
        tk.Button(self,text="Gráfica dirigida",font=('San Francisco', 20),width=50,height=3,cursor="heart",bg="#2d424a",
            command=lambda: [master.switch_frame(Directed)]).pack()
        #No dirigida
        tk.Button(self,text="Gráfica no dirigida",font=('San Francisco', 20),width=50,height=3,cursor="heart",bg="#5f6468",
            command=lambda: [master.switch_frame(NoDirected)]).pack()

"""         tk.Button(self, text="Regresar el menu Anterior",font=('San Francisco', 20),width=50,height=3,cursor="heart",bg="#b4786b",
                command=lambda: master.switch_frame(StartPage)).pack()  """