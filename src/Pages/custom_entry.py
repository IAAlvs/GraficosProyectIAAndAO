import tkinter as tk

class CustomEntry(tk.Entry):
    def __init__(self, master=None, textvariable=None, **kwargs):
        super().__init__(master, **kwargs)
        self.configure(textvariable=textvariable)
        self.text_variable = textvariable
        self.bind("<FocusIn>", self.on_entry_click)
        self.bind("<FocusOut>", self.on_entry_leave)
        self.bind("<KeyRelease>", self.validate_input)

    def on_entry_click(self, event):
        """Función que se ejecuta cuando se hace clic en el Entry."""
        if event.widget.get() == self.text_variable:
            event.widget.delete(0, tk.END)
            event.widget.config(fg='gray')

    def on_entry_leave(self, event):
        """Función que se ejecuta cuando se sale del Entry."""
        if event.widget.get() == '':
            event.widget.insert(0, self.text_variable)
            event.widget.config(fg='gray')
    def validate_input(self, event):
        entrada = event.widget.get()
        entrada = ''.join(c for c in entrada if c.isdigit())
        if(len(entrada)>2):
            entrada = entrada[:2]
        event.widget.delete(0, tk.END)  # Eliminar el texto existente
        event.widget.insert(0, entrada)