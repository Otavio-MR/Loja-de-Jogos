import tkinter as tk
from tkinter import messagebox


class AdicaoJogo(tk.Frame):
    def __init__(self, root, controller):
        self.root = root
        self.controller = controller
        self.frame = tk.Frame(self.root) # Frame Principal

        tk.Label(self.frame, text="Adicionar Jogo", font=("Arial", 16)).pack(pady=10)

        # Nome
        tk.Label(self.frame, text="Nome do Jogo:").pack(anchor="w", padx=10)
        self.nome = tk.Entry(self.frame, width=30)
        self.nome.pack(padx=10, pady=5)

        # Gênero
        tk.Label(self.frame, text="Gênero:").pack(anchor="w", padx=10)
        self.genero = tk.Entry(self.frame, width=30)
        self.genero.pack(padx=10, pady=5)

        # Preço
        tk.Label(self.frame, text="Preço (R$):").pack(anchor="w", padx=10)
        self.preco = tk.Entry(self.frame, width=30)
        self.preco.pack(padx=10, pady=5)

        # Botões
        tk.Button(self.frame, text="Adicionar", command=self.adicionar_jogo).pack(pady=5)
        tk.Button(self.frame, text="Voltar", command=self.controller.exibir_inicio).pack(pady=5)

    # Exibe a tela
    def mostrar(self):
        self.frame.pack()

    # Esconde a tela
    def esconder(self):
        self.frame.pack_forget()

    def limpar_campo(self):
        self.nome.delete(0, tk.END)
        self.genero.delete(0, tk.END)
        self.preco.delete(0, tk.END)

    def adicionar_jogo(self):
        nome = self.nome.get()
        genero = self.genero.get()
        preco = self.preco.get()
        sucesso, mensagem = self.controller.adicionar_jogo(nome, genero, preco)
        if sucesso:
            messagebox.showinfo("Sucesso", mensagem)
            self.controller.voltar_inicio()
        else:
            messagebox.showerror("Erro", "Informações Inválidas!")