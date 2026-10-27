import tkinter as tk
from tkinter import ttk

class EventoApp:
    def __init__(self,raiz):
        raiz.title("Evento de botão")
        self.label = ttk.Label(raiz, text="Olá , Tkinter!")
        self.label.pack(pady=10)
        botao = ttk.Button(raiz,text="Clique em mim",
                         command=self.clicando)
        botao.pack(pady=10)

    def clicando(self):
        self.label.config(text="Botão clicado!")

if __name__ == "__main__":
    raiz = tk.Tk()
    EventoApp(raiz)
    raiz.mainloop()