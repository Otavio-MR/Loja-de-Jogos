import tkinter as tk

class Carrinho:
    def __init__(self, root, view_controller):
        self.root = root
        self.view_controller = view_controller
        self.frame = tk.Frame(self.root) # Frame Principal

        tk.Label(self.frame, text="Carrinho", font=("Arial", 16)).pack(pady=10)

        # Onde os jogos do carrinho aparecem
        self.frm_lista = tk.Frame(self.frame)
        self.frm_lista.pack()

        # Onde vai aparecer o total da compra
        self.lbl_total = tk.Label(self.frame, text="Total: R$ 0.00", font=("Arial", 12))
        self.lbl_total.pack(pady=10)

        # Botões de ação de carrinho
        tk.Button(self.frame, text="Finalizar Compra", command=self.view_controller.processo_finalizacao_carrinho).pack(pady=5)
        tk.Button(self.frame, text="Voltar ao Catálogo", command=self.view_controller.ir_catalogo).pack(pady=5)

    # Exibe a tela
    def mostrar(self):
        self.frame.pack()

    # Esconde a tela
    def esconder(self):
        self.frame.pack_forget()

    # Atualiza a lista de jogos e o total
    def exibir_carrinho(self, itens, total):
        for widget in self.frm_lista.winfo_children():
            widget.destroy()

        for item in itens:
            txt = f"{item['nome']} | Quantidade: {item['quantidade']} | Preço: R$ {item['preco']:.2f}"
            frm_item = tk.Frame(self.frm_lista, relief=tk.RIDGE, borderwidth=1, padx=5, pady=5)
            frm_item.pack(pady=2, fill=tk.X)

            tk.Label(frm_item, text=txt).pack(side=tk.LEFT)
            tk.Button(frm_item, text="Remover Jogo", command=lambda j=item: self.view_controller.processo_remocao_produto(j)).pack(side=tk.RIGHT)

        self.lbl_total.config(text=f"Total: R$ {total:.2f}")