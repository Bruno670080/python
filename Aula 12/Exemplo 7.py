from pathlib import Path
from tkinter import Tk

janela = Tk()
janela.title("Nos amamos Python")
icone = Path (__file__).with_name("icon.ico")

if icone.exists():
    janela.iconbitmap(str(icone)) #Exemplo para Windows

janela.geometry("600x250")
janela.oval("tk: :PlaceWindow , center")
janela.mainloop