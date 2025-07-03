import tkinter as tk
from Controller.controller import Controller

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Loja de Jogos")
    root.geometry("500x300")
    root.resizable(True, True)
    app = Controller(root)
    root.mainloop()
