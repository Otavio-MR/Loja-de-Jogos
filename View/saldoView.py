import tkinter as tk

class Saldo:
    def __init__(self, root, view_controller):
        self.root = root
        self.view_controller = view_controller
        self.frame = tk.Frame(self.root) # Frame principal

        tk.Label(self.frame, text="Saldo", font=("Arial", 16)).pack(pady=10)

        # Saldo Atual
        self.lbl_saldo = tk.Label(self.frame, text="Saldo Atual: R$ 0,00", font=("Arial", 12))
        self.lbl_saldo.pack(pady=5)

        # Adição de Valor
        tk.Label(self.frame, text="Valor a adicionar:").pack(anchor="w", padx=10)
        self.valor = tk.Entry(self.frame, width=30)
        self.valor.pack(padx=10, pady=5)

        # Opções de Pagamento (Pix e Cartão)
        self.forma_pagamento = tk.StringVar(value="Pix")
        tk.Radiobutton(self.frame, text="Pix", variable=self.forma_pagamento, value="Pix").pack(anchor="w", padx=10)
        tk.Radiobutton(self.frame, text="Cartão", variable=self.forma_pagamento, value="Cartão").pack(anchor="w", padx=10)

        # Botões
        tk.Button(self.frame, text="Adicionar Saldo", command=self.processo_adicao_saldo).pack(pady=5)
        tk.Button(self.frame, text="Voltar", command=self.view_controller.ir_inicio).pack(pady=5)

    # Exibe a tela
    def mostrar(self):
        self.frame.pack()

    # Esconde a tela
    def esconder(self):
        self.frame.pack_forget()

    def atualizar(self, saldo):
        self.lbl_saldo.config(text=f"Saldo atual: R$ {saldo:.2f}")

    def processo_adicao_saldo(self):
        valor = self.valor.get()
        forma = self.forma_pagamento.get()
        # View chama a view principal (TkInterView), que chama o Controller
        self.view_controller.processo_adicao_saldo(valor, forma)
