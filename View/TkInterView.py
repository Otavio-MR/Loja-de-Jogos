import tkinter as tk
from View.inicioView import Inicio
from View.catalogoView import Catalogo
from View.carrinhoView import Carrinho
from View.adicaoJogoView import AdicaoJogo
from View.saldoView import Saldo
from View.historicoView import Historico
from tkinter import messagebox

class TkInterView:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Loja de Jogos")
        self.root.geometry("600x400")
        self.controller = None

        self.telas = {
            "inicio": Inicio(self.root, self),
            "catalogo": Catalogo(self.root, self),
            "carrinho": Carrinho(self.root, self),
            "saldo": Saldo(self.root, self),
            "historico": Historico(self.root, self),
            "adicao_jogo": AdicaoJogo(self.root, self),
        }

    def set_controller(self, controller):
        self.controller = controller

    def esconder_telas(self):
        for tela in self.telas.values():
            tela.esconder()

    # Metodos de exibição - View apenas exibe

    def mostrar_tela_inicio(self):
        self.esconder_telas()
        self.telas["inicio"].mostrar()

    def mostrar_tela_catalogo(self, jogos):
        self.esconder_telas()
        self.telas["catalogo"].exibir_jogos(jogos)
        self.telas["catalogo"].mostrar()

    def mostrar_tela_carrinho(self, itens, total):
        self.esconder_telas()
        self.telas["carrinho"].exibir_carrinho(itens, total)
        self.telas["carrinho"].mostrar()

    def mostrar_tela_saldo(self, saldo):
        self.esconder_telas()
        self.telas["saldo"].atualizar(saldo)
        self.telas["saldo"].mostrar()

    def mostrar_tela_adicao_jogo(self):
        self.esconder_telas()
        self.telas["adicao_jogo"].limpar_campo()
        self.telas["adicao_jogo"].mostrar()

    def mostrar_tela_historico(self, historico):
        self.esconder_telas()
        self.telas["historico"].exibir(historico)
        self.telas["historico"].mostrar()

    # Metodos para navegação - View chama o Controller

    def ir_catalogo(self):
        self.controller.ir_catalogo()

    def ir_carrinho(self):
        self.controller.ir_carrinho()

    def ir_adicao_jogo(self):
        self.controller.ir_adicao_jogo()

    def ir_saldo(self):
        self.controller.ir_saldo()

    def ir_historico(self):
        self.controller.ir_historico()

    def ir_inicio(self):
        self.controller.ir_inicio()

    # Metodos de ação - View chama o controller para processar

    def processo_adicao_jogo(self, nome, genero, preco):
        return self.controller.processo_adicao_jogo(nome, genero, preco)

    def processo_adicao_saldo(self, valor, forma_pagamento):
        return self.controller.processo_adicao_saldo(valor, forma_pagamento)

    def processo_finalizacao_carrinho(self):
        return self.controller.processo_finalizacao_carrinho()

    def processo_adicao_carrinho(self, jogo):
        return self.controller.processo_adicao_carrinho(jogo)

    def processo_remocao_produto(self, jogo):
        return self.controller.processo_remocao_produto(jogo)
    
    # Metodos de feedback - Controller chama a View para os resultados.

    def sucesso_adicao_jogo(self, mensagem):
        messagebox.showinfo("Sucesso!", mensagem)

    def erro_adicao_jogo(self, mensagem):
        messagebox.showerror("Erro!", mensagem)

    def sucesso_adicao_saldo(self, mensagem):
        messagebox.showinfo("Sucesso!", mensagem)

    def erro_adicao_saldo(self, mensagem):
        messagebox.showerror("Erro!", mensagem)

    def sucesso_adicao_carrinho(self, nome_jogo):
        messagebox.showinfo("Carrinho", f"{nome_jogo} adicionado ao carrinho!")

    def sucesso_compra(self, mensagem):
        messagebox.showinfo("Compra Finalizada!", mensagem)

    def erro_compra(self, mensagem):
        messagebox.showerror("Erro na Compra!", mensagem)

    # Metodos para rodar o app

    def iniciar_app(self):
        self.mostrar_tela_inicio()
        self.root.mainloop()

    def fechar_app(self):
        self.root.destroy()
