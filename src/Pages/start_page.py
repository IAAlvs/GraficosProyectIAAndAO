import tkinter as tk
from tkinter import *
try:
    import Tkinter as tk
except:
    import tkinter as tk
from Pages.directed import Directed
from Pages.no_directed import NoDirected

# Start page
class StartPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.configure(bg="#A8C3B7")
        self.pack(fill="both", expand=True)
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        mylabel = tk.Label(self, text="""
        Teoria de graficas:
        Alvarado Sanchez Isaac Alfredo
        Martinez Garcia Octavio Alan
        Elige la gráfica la cual quieres realizar
        
        
        
        """, font=('Arial', 16), bg="#A8C3B7")
        mylabel.pack(side="top", fill="x", pady=5)

        button1 = tk.Button(self, text="Gráfica dirigida", font=('Arial', 20), width=50, height=3,
                            cursor="hand2", bg="#2d424a", fg="#FFFFFF",
                            command=lambda: master.switch_frame(Directed))
        button1.pack(pady=10)

        button2 = tk.Button(self, text="Gráfica no dirigida", font=('Arial', 20), width=50, height=3,
                            cursor="hand2", bg="#5f6468", fg="#FFFFFF",
                            command=lambda: master.switch_frame(NoDirected))
        button2.pack(pady=10)

        button3 = tk.Button(self, text="Cerrar aplicación", font=('Arial', 16), width=20, height=2,
                            cursor="hand2", bg="#BF4040", fg="#FFFFFF",
                            command=self.quit)
        button3.pack(pady=10)

