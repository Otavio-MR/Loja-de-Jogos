import tkinter as tk
from tkinter import messagebox


class Catalogo:
    def __init__(self, root, controller):
        self.root = root
        self.controller = controller
        self.frame = tk.Frame(self.root) # Frame principal
        self.lbl_jogos = []

        tk.Label(self.frame, text="Catálogo", font=("Arial", 16)).pack(pady=10)

        # Frame que lista os jogos
        self.frm_lista = tk.Frame(self.frame)
        self.frm_lista.pack()

        # Botões para acessar o carrinho
        tk.Button(self.frame, text="Ver o Carrinho", command=self.controller.mostrar_carrinho).pack(pady=5)
        tk.Button(self.frame, text="Voltar", command=self.controller.voltar_inicio).pack(pady=5)

    # Exibe a tela
    def mostrar(self):
        self.frame.pack()

    # Esconde a tela
    def esconder(self):
        self.frame.pack_forget()

    # Lista todos os jogos na interface
    def exibir_jogos(self, lista_jogos):
        # Limpa a lista antiga
        for widget in self.frm_lista.winfo_children():
            widget.destroy()

        for jogo in lista_jogos:
            frm_jogo = tk.Frame(self.frm_lista, relief=tk.RIDGE, borderwidth=2, padx=5, pady=5)
            frm_jogo.pack(pady=5, fill=tk.X)

            txt = f"Nome: {jogo['nome']} | Gênero: {jogo["genero"]} | Preço: R${jogo["preco"]:.2f}"
            tk.Label(frm_jogo, text=txt).pack(side=tk.LEFT)

            # Botão de Adicionar no Carrinho
            tk.Button(frm_jogo, text="Adicionar ao Carrinho", command=lambda j=jogo: self.add_feedback(j)).pack(side=tk.RIGHT)

    def add_feedback(self, jogo):
        self.controller.adicao_carrinho(jogo)
        messagebox.showinfo("Carrinho", f"{jogo['nome']} adicionado ao carrinho!")

