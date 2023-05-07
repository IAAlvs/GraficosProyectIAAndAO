import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from Pages.show_matrix import ShowMatrix
from Pages.my_matrix import MyMatrix
import random
import math



class Directed(tk.Frame):
    def __init__(self, master):
        #Import because cicular import
        from Pages.start_page import StartPage
        super().__init__(master=master)
        self.canvas = tk.Canvas(self, width=600, height=400, bg='white')
        self.canvas.pack(fill=tk.BOTH, expand=True)
        self.nodes = []
        self.connections = []
        self.selected_node = None
        self.add_node_button = tk.Button(self, text="Agregar nodo", command=self.add_node, background="#32CD32")
        self.add_node_button.pack(side=tk.LEFT)
        self.delete_node_entry = tk.Entry(self, width=5, background="#FF6347")
        self.delete_node_entry.pack(side=tk.LEFT)
        self.delete_node_button = tk.Button(self, text="Eliminar Nodo", command=self.delete_node, background="#FF6347")
        self.delete_node_button.pack(side=tk.LEFT)
        self.add_connection_node1_entry = tk.Entry(self,highlightthickness=2, highlightcolor="#1E90FF", width=5, textvariable="desde")
        self.add_connection_node1_entry.insert(0, 'Inicio')
        self.add_connection_node1_entry.bind('<FocusIn>', lambda event: self.on_entry_click(event,"Inicio"))
        self.add_connection_node1_entry.bind('<FocusOut>', lambda event: self.on_entry_leave(event, "Inicio"))
        self.add_connection_node1_entry.pack(side=tk.LEFT)

        self.add_connection_node2_entry = tk.Entry(self, insertbackground="gray", width=5,highlightthickness=2, highlightcolor="#1E90FF", textvariable="Fin")
        self.add_connection_node2_entry.insert(0, 'Fin')
        self.add_connection_node2_entry.bind('<FocusIn>', lambda event: self.on_entry_click(event,"Fin"))
        self.add_connection_node2_entry.bind('<FocusOut>', lambda event: self.on_entry_leave(event, "Fin"))
        self.add_connection_node2_entry.pack(side=tk.LEFT)
        self.add_connection_button = tk.Button(self, text="Agregar conexion",background="#1E90FF", command=self.add_connection)
        self.add_connection_button.pack(side=tk.LEFT)
        self.show_adjacency_matrix = tk.Button(self, text="Generar matriz de adyacencia", command = self.show_adjacency_matrix).pack()
        self.show_incidency_matrix = tk.Button(self, text="Generar matriz de incidencia", command = self.show_incidency_matrix).pack()

        self.prev_menu = tk.Button(self, text="Regresar al menú anterior", 
                                   command=lambda: [master.switch_frame(StartPage)]).pack(side=tk.LEFT)


    @property
    def node_size(self):
        return 20
    def get_node_by_id(self, node_id):
        for node in self.nodes:
            if node.get("id") == node_id:
                return node
        messagebox.showerror("Error","Alguno de los nodos no existe")
        print("Se trato de recuperar un nodo inexistente")
        return None

    def add_node(self):
        x = random.randint(self.node_size, self.canvas.winfo_width() - self.node_size)
        y = random.randint(self.node_size, self.canvas.winfo_height() - self.node_size)
        node_id = len(self.nodes)
        node_color = '#{:06x}'.format(random.randint(0, 0xFFFFFF))
        node = self.canvas.create_oval(x - self.node_size, y - self.node_size, x + self.node_size, y + self.node_size, fill=node_color, outline='black', width=2, tags=('node', 'node-{}'.format(node_id)))
        text = self.canvas.create_text(x, y, text=str(node_id), tags=("text", f"text-{node_id}"))
        node_element = {"id": node_id, "x": x, "y": y, "text" : f"text-{node_id}", "node" : f"node-{node_id}"}
        self.nodes.append(node_element)
        self.canvas.tag_bind(node, '<Button-1>', lambda event, node_id=node_id: self.select_node(node_id))
    def delete_node(self):
        #Deletes everything about a node conections, register, form
        node_id = self.delete_node_entry.get()
        if(node_id is None or node_id == ""):
            messagebox.showinfo("Atento", "Es necesario un nodo para hacer la acción")
            return
        node_id = int(self.delete_node_entry.get())
        if any(ndict["id"] == node_id for ndict in self.nodes) is False :
            messagebox.showerror("Error", f"El nodo {node_id} no existe")
            return
        node = self.get_node_by_id(node_id)
        # Delete the connections
        for connection in self.connections:
            #delete lines
            if(connection["from"] == node_id or connection["to"] == node_id):
                #Eliminamos las lineas y demas elementos relacionados con la conexion
                self.canvas.delete(connection["connection_id"])
                #Eliminamos del array para que ya no exista esa vieja conexion
                self.connections.remove(connection)
        #Voy a repetir el algoritmo por que con una sola pasada no se eliminan todas las lineas
        #xdxdxdxd
        for connection in self.connections:
            #delete lines
            if(connection["from"] == node_id or connection["to"] == node_id):
                #Eliminamos las lineas y demas elementos relacionados con la conexion
                self.canvas.delete(connection["connection_id"])
                #Eliminamos del array para que ya no exista esa vieja conexion
                self.connections.remove(connection)


        # Delete the node from the canvas
        self.canvas.delete(node["text"])
        
        # Delete the node from the graph
        self.canvas.delete(node["node"])
        self.nodes.remove(node)
        print("CONECCIONES DESPUES DE SER ELIMINADAS =====")
        print(self.connections)

        messagebox.showinfo("Success", f"Nodo {node_id} y sus conexiones eliminadas.")

    
    def add_connection(self):
        """
        Add a connection between two nodes based on the user's input in the entry boxes.
        """
        start_node = self.add_connection_node1_entry.get()
        end_node = self.add_connection_node2_entry.get()
        if(start_node == "" or end_node == ""):
            messagebox.showinfo("Atento","Los dos nodos son necesarios para completar la acción")
            return
        start_node = int(self.add_connection_node1_entry.get())
        end_node = int(self.add_connection_node2_entry.get())
        if(any(ndict["id"] == start_node for ndict in self.nodes) is False and
           any(ndict["id"] != end_node for ndict in self.nodes) is False):
            messagebox.showerror("Error","Alguno de los nodos no existe")
            return
        #if start_node == end_node:
            #messagebox.showerror("Error", "El nodo inicial no puede ser el mismo al final.")
        MAX_PARALEL_LINES = 3 
        paralel_lines = 0
        for diccionario in self.connections:
            if ((diccionario["from"] == start_node and diccionario["to"] == end_node)or 
                (diccionario["to"] == start_node and diccionario["from"] == end_node)
                ):
                paralel_lines += 1
        if(paralel_lines > MAX_PARALEL_LINES):
            messagebox.showinfo("Atento", "No puede haber más de 3 lineas paralelas")
            return
        #if is a pararalel linea we add _NUMBEROFPARALELLINE to connection_id
        connection_id = (f"c{start_node}{end_node}" if 
                        (paralel_lines == 0) 
                        else f"c{start_node}{end_node}_{paralel_lines}")
        if(paralel_lines > 0 ):
            self.connections.append({"from":start_node,"to":end_node, "connection_id" : connection_id})
            self.draw_radius_line(start_node, end_node, connection_id, paralel_lines)
            messagebox.showinfo("Bien", f"Conexion entre los nodos {start_node} y {end_node} hecha.")
            return
        #Para este caso dibujaremos un arco 
        self.connections.append({"from":start_node,"to":end_node, "connection_id" : connection_id})
        self.draw_line(start_node, end_node, connection_id)
        messagebox.showinfo("Bien", f"Conexion entre los nodos {start_node} y {end_node} hecha.")
        print(self.connections)
    def remove_connection(self):
        """
        Remove a connection between two nodes based on the user's input in the entry boxes.
        """
        start_node = int(self.start_node_input.get())
        end_node = int(self.end_node_input.get())

        if not self.graph.has_connection(start_node, end_node):
            messagebox.showerror("Error", "Conexión entre los nodos no existe")
        else:
            self.graph.remove_connection(start_node, end_node)
            self.draw_graph()
            messagebox.showinfo("Success", f"Connection between nodes {start_node} and {end_node} removed.")
    def update_connection_tags(self):
        """
        Update the tags for all the connection lines on the canvas.
        """
        for node_id, (oval, _) in self.node_objects.items():
            for connected_node_id in self.graph.get_connected_nodes(node_id):
                connected_oval, _ = self.node_objects[connected_node_id]
                line = self.canvas.find_withtag(f"line_{node_id}_{connected_node_id}")[0]
                self.canvas.itemconfig(line, tags=(oval, connected_oval, f"line_{node_id}_{connected_node_id}"))
    def draw_line(self, start_node, end_node, connection_id):
        # Limpiar canvas
        #self.canvas.delete("all")
        start_node = self.get_node_by_id(start_node)
        end_node = self.get_node_by_id(end_node)
        if(start_node is None or end_node is None):
            return
        #TO ADD ARROW WE USE PARAMETER arrow=tk.LAST
        if(start_node == end_node):
            x1,y1 = start_node["x"], start_node["y"] # Obtenemos las coordenadas del ovalo
            self.canvas.create_arc([(x1),y1-30,(x1 + 30),  y1+30,], start= 0, extent = 180,
                style='pieslice', width=2, outline='black',tags=("connection", connection_id))
            self.canvas.create_text(x1+30, y1-35, text=connection_id,
                        fill="black", tags=("connection", connection_id))
            
        else:  
            x1,y1 = start_node["x"], start_node["y"]
            x2,y2 = end_node["x"], end_node["y"]
            self.canvas.create_line(x1, y1,
                x2, y2, arrow=tk.LAST, width=4, 
                tags=("connection", connection_id))
            self.canvas.create_text((x1+x2)/2, (y1+y2)/2, text=connection_id,
                                    fill="black", tags=("connection", connection_id))
    def draw_radius_line(self, start_node, end_node, connection_id, paralel_number):
        # Limpiar canvas
        #self.canvas.delete("all")
        start_node = self.get_node_by_id(start_node)
        end_node = self.get_node_by_id(end_node)
        if(start_node is None or end_node is None):
            return
        #TO ADD ARROW WE USE PARAMETER arrow=tk.LAST
        #Case when we have a loop
        if(start_node == end_node):
            x1,y1 = start_node["x"], start_node["y"] # Obtenemos las coordenadas del ovalo
            self.canvas.create_arc([(x1),y1-30,(x1 + 30),  y1+30,],
                style='pieslice', width=4, outline='black',tags=("connection", connection_id))
            self.canvas.create_text(x1+30, y1-35, text=connection_id,
                        fill="black", tags=("connection", connection_id))
        else:  

            x1,y1 = start_node["x"], start_node["y"] # Obtenemos las coordenadas del ovalo
            x2, y2 = end_node["x"], end_node["y"]
            number_to_add = 15 if paralel_number==1 else -15
            self.canvas.create_line(x1+number_to_add, y1+number_to_add,
                x2+number_to_add, y2+number_to_add, arrow=tk.LAST, width=4, 
                tags=("connection", connection_id))
            text = self.canvas.create_text(((x1+x2)/2)+number_to_add, ((y1+y2)/2)+number_to_add, text=connection_id,
                        fill="black", tags=("connection", connection_id))    
    def generate_adjacency_matrix(self) -> MyMatrix:
        #This implementation is for not directed graph
        connections = self.connections
        nodes = self.nodes
        num_nodes = len(nodes)
        adj_matrix = [[0] * num_nodes for _ in range(num_nodes)]
        for connection in connections:
            from_idx = connection['from']
            to_idx =  connection['to']
            #For directed graph only change implementation
            adj_matrix[from_idx][to_idx] = 1
            #adj_matrix[to_idx][from_idx] = 1
        upper_headers = [str(i) for i in range(len(adj_matrix))]
        side_headers = [str(i) for i in range(len(adj_matrix))]
        return MyMatrix(adj_matrix, "Matriz de adyacencia", upper_headers, side_headers)
    def generate_incidency_matrix(self) -> MyMatrix:
        connections = self.connections
        nodes = self.nodes
        num_nodes = len(nodes)
        lines_set = list(map(lambda c: c['connection_id'], connections))
        lines_num = len(lines_set)
        #we denote as set but i s not a set because every node has a unique id
        nodes_set = list(map(lambda n: n['id'], self.nodes))
        inc_matrix = [[0] * lines_num for _ in range(num_nodes)]
        for i, connection in enumerate(connections):
            for j,node in enumerate(nodes):
                if(connection["from"] == node["id"]):
                    inc_matrix[j][i] = 1 
                if(connection["to"] == node["id"]):
                    inc_matrix[j][i] = -1
        return MyMatrix(inc_matrix, "Matriz de incidencia", list(lines_set), nodes_set)
    def show_adjacency_matrix(self):
        matrix = self.generate_adjacency_matrix()
        ventana_matriz = ShowMatrix(matrix)
        ventana_matriz.mainloop()
    def show_incidency_matrix(self):
        matrix = self.generate_incidency_matrix()
        ventana_matriz = ShowMatrix(matrix)
        ventana_matriz.mainloop()
    def on_entry_click(self, event, text):
        """Función que se ejecuta cuando se hace clic en el Entry."""
        if event.widget.get() == text:
            event.widget.delete(0, tk.END)
            event.widget.config(fg='gray')

    def on_entry_leave(selv, event, text):
        """Función que se ejecuta cuando se sale del Entry."""
        if event.widget.get() == '':
            event.widget.insert(0, text)
            event.widget.config(fg='gray')
