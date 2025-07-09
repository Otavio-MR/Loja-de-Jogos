import tkinter as tk
from View.inicioView import Inicio
from View.catalogoView import Catalogo
from View.carrinhoView import Carrinho
from View.adicaoJogoView import AdicaoJogo
from View.saldoView import Saldo
from View.historicoView import Historico

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

    def iniciar_app(self):
        self.mostrar_tela_inicio()
        self.root.mainloop()

    def fechar_app(self):
        self.root.destroy()

    def mostrar_catalogo(self):
        self.controller.ir_catalogo()

    def mostrar_carrinho(self):
        self.controller.ir_carrinho()

    def mostrar_adicao(self):
        self.controller.ir_adicao_jogo()

    def mostrar_saldo(self):
        self.controller.ir_saldo()

    def mostrar_historico(self):
        self.controller.ir_historico()

    def voltar_inicio(self):
        self.controller.ir_inicio()

    def adicionar_jogo(self, nome, genero, preco):
        return self.controller.adicionar_jogo(nome, genero, preco)

    def adicao_saldo(self, valor, forma_pagamento):
        return self.controller.adicao_saldo(valor, forma_pagamento)

    def finalizar_carrinho(self):
        return self.controller.finalizar_carrinho()

    def adicao_carrinho(self, jogo):
        return self.controller.adicao_carrinho(jogo)

    def remover_produto(self, jogo):
        return self.controller.remover_produto(jogo)