import tkinter as tk
from tkinter import *
try:
    import Tkinter as tk
except:
    import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import networkx as nx
#Clase Encarga del funcionamiento de la grafica dirigida
class Directed(tk.Frame):
    
    def __init__(self, master):#Constructor
        """         from Pages.start_page import StartPage
        global ec1,puntoinicio,derivada,ci
        des1="Crear la grafica conectando con el nodo que tiene relación"
        ec1=StringVar()
        puntoinicio=StringVar()
        tk.Frame.__init__(self, master)
        tk.Frame.configure(self,bg="#A8C3B7") """
        super().__init__(master)
        self.master = master
        self.create_widgets()
        # Inicializa el grafo dirigido vacío y un diccionario para almacenar los nodos
        self.graph = nx.DiGraph()
        self.node_dict = {}

        # Configura la capacidad de arrastrar y soltar nodos
        self.dragged = None
        self.canvas.tag_bind('node', '<Button-1>', self.click)
        self.canvas.tag_bind('node', '<Button1-Motion>', self.drag)
        self.canvas.tag_bind('node', '<ButtonRelease-1>', self.drop)

    def create_widgets(self):
        # Crea una figura
        fig = Figure()

        # Crea una subfigura
        ax = fig.add_subplot(111)

        # Dibuja el grafo vacío en la subfigura
        nx.draw(self.graph, ax=ax, with_labels=True)

        # Crea un widget de lienzo
        canvas = FigureCanvasTkAgg(fig, master=self)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

        # Crea un botón para limpiar el grafo
        clear_button = tk.Button(master=self, text="Limpiar", command=self.clear)
        clear_button.pack(side=tk.BOTTOM)

        # Guarda la subfigura y el widget de lienzo en la clase
        self.ax = ax
        self.canvas = canvas.get_tk_widget()

    def add_node(self, event):
        # Agrega un nodo a la posición del evento del ratón
        node_id = len(self.node_dict)
        x, y = self.canvas.canvasx(event.x), self.canvas.canvasy(event.y)
        self.node_dict[node_id] = self.graph.add_node(node_id, pos=(x, y))

        # Dibuja el nuevo nodo
        circle = self.ax.add_patch(plt.Circle((x, y), radius=0.1, color='r', alpha=0.5))
        self.canvas.create_text(x, y, text=node_id, tags=('node',), fill='white')

    def click(self, event):
        # Al hacer clic en un nodo, lo marca como arrastrado
        item = self.canvas.find_withtag(tk.CURRENT)
        if item:
            self.dragged = item[0]

    def drag(self, event):
        # Al arrastrar un nodo, lo mueve a la posición del cursor
        if self.dragged:
            x, y = self.canvas.canvasx(event.x), self.canvas.canvasy(event.y)
            self.canvas.coords(self.dragged, x-10, y-10, x+10, y+10)

    def drop(self, event):
        # Al soltar un nodo arrastrado, lo suelta y verifica si se conecta a otro nodo
        if self.dragged:
            item = self.canvas.find_overlapping(event.x, event.y, event.x, event.y)
            if item:
                if item[0] != self.dragged:
                    # Si se encuentra un nodo diferente al nodo arrastrado, se conecta
                    node

        tk.Label(self, text=des1,font=('San Francisco',11),width=100,height=2,bg="#A8C3B7").pack(side="top", fill="x", pady=5)
        tk.Button(self,text=" Presiona Regresar",cursor="hand2",height=2,command=lambda: [master.switch_frame(StartPage)]).pack()

