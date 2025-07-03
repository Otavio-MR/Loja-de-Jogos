import tkinter as tk

class Inicio:
    def __init__(self, root, controller):
        self.root = root
        self.controller = controller
        self.frame = tk.Frame(self.root) # Frame principal da tela

        # Título da tela
        tk.Label(self.frame, text="Loja de Jogos", font=("Arial", 20)).pack(pady=10)

        # Botões da Tela do Inicio
        tk.Button(self.frame, text="Ir ás compras", command=self.controller.mostrar_catalogo).pack(pady=5)
        tk.Button(self.frame, text="Ver histórico", command=self.controller.mostrar_historico).pack(pady=5)
        tk.Button(self.frame, text="Adicionar Jogos", command=self.controller.mostrar_adicao).pack(pady=5)
        tk.Button(self.frame, text="Adicionar/Ver Saldo", command=self.controller.mostrar_saldo).pack(pady=5)
        tk.Button(self.frame, text="Sair", command=self.root.quit).pack(pady=10)

    # Exibe a tela
    def mostrar(self):
        self.frame.pack()

    # Esconde a tela
    def esconder(self):
        self.frame.pack_forget()