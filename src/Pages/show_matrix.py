import tkinter as tk
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class ShowMatrix(tk.Toplevel):
    def __init__(self, matriz, matrix_type):
        super().__init__()
        self.title(matrix_type)
        self.geometry("400x400")
        # Crear encabezados de columna y fila a partir de números secuenciales
        encabezados = [str(i) for i in range(len(matriz))]

        # Convertir matriz a una matriz NumPy
        matriz_np = np.array(matriz)

        # Crear un gráfico de matriz con Matplotlib
        fig, ax = plt.subplots()
        im = ax.imshow(matriz_np)

        # Añadir etiquetas de columna y fila
        ax.set_xticks(np.arange(len(encabezados)))
        ax.set_yticks(np.arange(len(encabezados)))
        ax.set_xticklabels(encabezados)
        ax.set_yticklabels(encabezados)

        # Rotar las etiquetas de columna para que sean más legibles
        plt.setp(ax.get_xticklabels(), rotation=45, ha="right",
                 rotation_mode="anchor")

        # Añadir los valores de la matriz a cada celda
        for i in range(len(encabezados)):
            for j in range(len(encabezados)):
                text = ax.text(j, i, matriz_np[i, j],
                               ha="center", va="center", color="w")

        # Añadir un título para el gráfico
        ax.set_title("Matriz de adyacencia")

        # Ajustar el diseño del gráfico para que se ajuste a la ventana
        fig.tight_layout()

        # Mostrar el gráfico en un widget FigureCanvasTkAgg de Matplotlib
        canvas = FigureCanvasTkAgg(fig, master=self)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        # Crear un botón para cerrar la ventana
        boton_cerrar = tk.Button(self, text="Cerrar", command=self.destroy)
        boton_cerrar.pack(pady=10)