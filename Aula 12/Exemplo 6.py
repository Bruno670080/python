import tkinter as tk
from tkinter import ttk

class MesesApp:
    def __init__(self, raiz):
        raiz.geometry("270x130")
        raiz.title("Exemplo de combobx")
        ttk.Label(raiz, text = "Selecione um mês:").pack(pady = 5)
        meses=["Janeiro","Fevereiro","Março","Abril","Maio","Junho","Julho","Agosto","Setembro","Outubro","Novembro", "Dezembro"]
        self.combo = ttk.Combobox(raiz, values=meses, state ="readonly")
        self.combo.pack(pady=5)
        self.combo.current(0)
        self.combo.bind("<<ComboboxSelected>>", self.selecionar)

    def selecionar(self, _):
        print(f"Mês escolhido: {self.combo.get()}")

if __name__ == "__main__":
    raiz = tk.Tk()
    MesesApp(raiz)
    raiz.mainloop()