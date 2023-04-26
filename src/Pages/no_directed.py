import tkinter as tk
from tkinter import *
try:
    import Tkinter as tk
except:
    import tkinter as tk

#Clase Encargada del funcionamiento de la grafica no dirigida
class NoDirected(tk.Frame):
      def __init__(self, master):#Constructor
        from Pages.start_page import StartPage
        global ec2,puntoinicio1,puntoinicio2,redondeo
        ec2=StringVar()
        des2="Crea la grafica conectando hacia el nodo"
        puntoinicio1=StringVar()
        puntoinicio2=StringVar()
        cifras2=StringVar()
        tk.Frame.__init__(self, master)
        tk.Frame.configure(self,bg="#A8C3B7")
        tk.Label(self, text=des2,font=('San Francisco',11),width=100,height=2,bg="#A8C3B7").pack(side="top", fill="x", pady=5)
        tk.Button(self,text=" Presiona Regresar",cursor="hand2",height=2,command=lambda: [master.switch_frame(StartPage)]).pack()

