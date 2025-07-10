import tkinter as tk

class Historico:
    def __init__(self, root, view_controller):
        self.root = root
        self.view_controller = view_controller
        self.frame = tk.Frame(self.root) # Frame principal

        tk.Label(self.frame, text="Histórico", font=("Arial", 16)).pack(pady=10)

        # Frame onde os registros de compras aparecem
        self.frm_lista = tk.Frame(self.frame)
        self.frm_lista.pack(padx=10, pady=5)

        # Botão Voltar
        tk.Button(self.frame, text="Voltar", command=self.view_controller.ir_inicio).pack(pady=5)

    def mostrar(self):
        self.frame.pack()

    def esconder(self):
        self.frame.pack_forget()

    def exibir(self, historico):
        # Limpa a lista anterior
        for widget in self.frm_lista.winfo_children():
            widget.destroy()

        if not historico:
            tk.Label(self.frm_lista, text="Nenhuma compra realizada ainda!").pack()
            return

        # Exibe uma compra por vez
        for compra in historico:
            frm_compra = tk.Frame(self.frm_lista, relief=tk.RIDGE, borderwidth=1, padx=5, pady=5)
            frm_compra.pack(fill=tk.X, pady=5)

            data = compra.get("data", "Data Desconhecida")
            total = compra.get("total", 0.0)
            jogos = compra.get("jogos", [])

            # Titulo da Compra
            tk.Label(self.frm_lista, text=f"Data: {data} | Total: R$ {total:.2f}", font=("Arial", 10, "bold")).pack(anchor="w")

            for jogo in compra['jogos']:
                if isinstance(jogo, dict):
                    nome = jogo.get("nome", "Jogo Desconhecido")
                    quantidade = jogo.get("quantidade", 1)
                    preco_total = jogo.get("preco_total", 0.0)

                    tk.Label(self.frm_lista, text=f"- {nome} (x{quantidade}) | Total: R$ {preco_total:.2f}").pack(anchor="w", padx=20)
