import tkinter as tk
from tkinter import messagebox
import random
import math

class Directed(tk.Frame):
    def __init__(self, master=None, **kwargs):
        super().__init__(master=master, **kwargs)
        self.canvas = tk.Canvas(self, width=600, height=400, bg='white')
        self.canvas.pack(fill=tk.BOTH, expand=True)
        self.nodes = []
        self.connections = []
        self.selected_node = None
        self.add_node_button = tk.Button(self, text="Add Node", command=self.add_node)
        self.add_node_button.pack(side=tk.LEFT)
        self.delete_node_entry = tk.Entry(self, width=5)
        self.delete_node_entry.pack(side=tk.LEFT)
        self.delete_node_button = tk.Button(self, text="Delete Node", command=self.delete_node)
        self.delete_node_button.pack(side=tk.LEFT)
        self.add_connection_node1_entry = tk.Entry(self, width=5)
        self.add_connection_node1_entry.pack(side=tk.LEFT)
        self.add_connection_node2_entry = tk.Entry(self, width=5)
        self.add_connection_node2_entry.pack(side=tk.LEFT)
        self.add_connection_button = tk.Button(self, text="Add Connection", command=self.add_connection)
        self.add_connection_button.pack(side=tk.LEFT)
        self.remove_connection_node1_entry = tk.Entry(self, width=5)
        self.remove_connection_node1_entry.pack(side=tk.LEFT)
        self.remove_connection_node2_entry = tk.Entry(self, width=5)
        self.remove_connection_node2_entry.pack(side=tk.LEFT)
        self.remove_connection_button = tk.Button(self, text="Remove Connection", command=self.remove_connection)
        self.remove_connection_button.pack(side=tk.LEFT)

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
        text = self.canvas.create_text(x, y, text=str(node_id), tags=())
        node_element = {"id": node_id, "x": x, "y": y, "text" : text, "oval" : node}
        self.nodes.append(node_element)
        self.canvas.tag_bind(node, '<Button-1>', lambda event, node_id=node_id: self.select_node(node_id))
    def delete_node(self):
        node_id = int(self.delete_node_entry.get())
        if self.nodes[node_id] is None:
            messagebox.showerror("Error", f"El nodo {node_id} no existe")
            return
        if node_id >= len(self.nodes):
            return
        # Delete the connections to this node
        for connected_node_id in self.graph.get_connected_nodes(node_id):
            self.graph.remove_connection(node_id, connected_node_id)
            self.delete_connection(node_id, connected_node_id)

        # Delete the node from the graph
        self.graph.remove_node(node_id)

        # Delete the node from the canvas
        oval, text = self.node_objects.pop(node_id)
        self.canvas.delete(oval)
        self.canvas.delete(text)

        # Update the connection tags
        self.update_connection_tags()

        messagebox.showinfo("Success", f"Node {node_id} deleted.")
        node = self.nodes[node_id]
        self.canvas.delete(node)
        self.nodes.pop(node_id)
        #self.update_connection_tags()

    
    def add_connection(self):
        """
        Add a connection between two nodes based on the user's input in the entry boxes.
        """
        start_node = int(self.add_connection_node1_entry.get())
        end_node = int(self.add_connection_node2_entry.get())
        """         print(self.nodes)
        print(any(ndict["id"] == start_node for ndict in self.nodes))
        print(any(ndict["id"] == end_node for ndict in self.nodes) """
        if(any(ndict["id"] == start_node for ndict in self.nodes) is False and
           any(ndict["id"] != end_node for ndict in self.nodes) is False):
            messagebox.showerror("Error","Alguno de los nodos no existe")
            return
        if start_node == end_node:
            messagebox.showerror("Error", "El nodo inicial no puede ser el mismo al final.")
        for diccionario in self.connections:
            if (diccionario["from"] == start_node and diccionario["to"] == end_node):
                messagebox.showerror("Error", "La conexion ya  existe.")
                return
        else:
            self.connections.append({"from":start_node,"to":end_node, "connection_id" : f"{start_node}{end_node}"})
            self.draw_graph(start_node, end_node )
            messagebox.showinfo("Bien", f"Conexion entre los nodos{start_node} y {end_node} hecha.")
    def remove_connection(self):
        """
        Remove a connection between two nodes based on the user's input in the entry boxes.
        """
        start_node = int(self.start_node_input.get())
        end_node = int(self.end_node_input.get())

        if not self.graph.has_connection(start_node, end_node):
            messagebox.showerror("Error", "Connection does not exist.")
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
    def draw_graph(self, start_node, end_node):
        # Limpiar canvas
        #self.canvas.delete("all")
        start_node = self.get_node_by_id(start_node)
        end_node = self.get_node_by_id(end_node)
        if(start_node is None or end_node is None):
            return
        #TO ADD ARROW WE USE PARAMETER arrow=tk.LAST
        self.canvas.create_line(start_node["x"], start_node["y"], end_node["x"], end_node["y"], tags=("connection", str(start_node["id"]), str(end_node["id"])))
    def get_contour_coordinates(self, node1, node2):
        x1, y1 = [node1["x"], node1["y"] ]
        x2, y2 = [node2["x"], node2["y"]  ]
        x, y = x1, y1
        dx, dy = x2 - x1, y2 - y1
        length = math.sqrt(dx*dx + dy*dy)
        dx, dy = dx/length, dy/length
        x2, y2 = x + dx*(node1.node_size+5), y + dy*(node1.node_size+5)
    
        return []
            