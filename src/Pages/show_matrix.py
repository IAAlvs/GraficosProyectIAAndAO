import tkinter as tk
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from Pages.my_matrix import MyMatrix

class ShowMatrix(tk.Toplevel):
    def __init__(self, my_matrix : MyMatrix ):
        super().__init__()
        matriz = my_matrix.matrix
        matrix_type = my_matrix.matrix_name
        upper_headers = my_matrix.upper_headers
        side_headers = my_matrix.side_headers
        self.title(matrix_type)
        self.geometry("400x400")

        # Crear encabezados de columna y fila a partir de números secuenciales
        #encabezados = [str(i) for i in range(len(matriz))]

        # Convertir matriz a una matriz NumPy
        matriz_np = np.array(matriz)

        # Crear un gráfico de matriz con Matplotlib
        fig, ax = plt.subplots()
        im = ax.imshow(matriz_np)

        # Añadir etiquetas de columna y fila
        ax.set_xticks(np.arange(len(upper_headers)))
        ax.set_yticks(np.arange(len(side_headers)))
        ax.set_xticklabels(upper_headers)
        ax.set_yticklabels(side_headers)

        # Rotar las etiquetas de columna para que sean más legibles
        plt.setp(ax.get_xticklabels(), rotation=45, ha="right",
                 rotation_mode="anchor")

        # Añadir los valores de la matriz a cada celda
        for i in range(len(side_headers)):
            for j in range(len(upper_headers)):
                text = ax.text(j, i, matriz_np[i, j],
                               ha="center", va="center", color="w")

        # Añadir un título para el gráfico
        ax.set_title(matrix_type)

        # Ajustar el diseño del gráfico para que se ajuste a la ventana
        fig.tight_layout()

        # Mostrar el gráfico en un widget FigureCanvasTkAgg de Matplotlib
        canvas = FigureCanvasTkAgg(fig, master=self)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        # Crear un botón para cerrar la ventana
        boton_cerrar = tk.Button(self, text="Cerrar", command=self.destroy)
        boton_cerrar.pack(pady=10)