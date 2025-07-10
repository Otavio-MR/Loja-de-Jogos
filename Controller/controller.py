from Model.mongoModel import Mongo
from Model.carrinhoModel import Carrinho
from Model.saldoModel import Saldo
from Model.jogoModel import Jogo
from Model.compraModel import Compra

class Controller:
    def __init__(self):
        self.mongo = Mongo()
        self.saldo_model = Saldo(self.mongo, self.mongo.carregar_saldo())
        self.jogo_model = Jogo(self.mongo)
        self.carrinho_model = Carrinho()
        self.compra_model = Compra(self.mongo, self.carrinho_model, self.saldo_model)

        self.view = None

    def set_view(self, view):
        self.view = view

    def ir_inicio(self):
        self.view.mostrar_tela_inicio()

    def ir_catalogo(self):
        jogos = self.mongo.lista_jogos()
        self.view.mostrar_tela_catalogo(jogos)

    def ir_carrinho(self):
        total = self.carrinho_model.calculo_total()
        jogos_carrinho = self.carrinho_model.produtos
        self.view.mostrar_tela_carrinho(jogos_carrinho, total)

    def ir_adicao_jogo(self):
        self.view.mostrar_tela_adicao_jogo()

    def ir_saldo(self):
        saldo = self.saldo_model.get_saldo()
        self.view.mostrar_tela_saldo(saldo)

    def ir_historico(self):
        historico = self.mongo.lista_historico()
        self.view.mostrar_tela_historico(historico)

    def processo_adicao_jogo(self, nome, genero, preco):
        sucesso, mensagem = self.jogo_model.criar_jogo(nome, genero, preco)
        if sucesso:
            self.view.sucesso_adicao_jogo(mensagem)
            self.ir_inicio()
        else:
            self.view.erro_adicao_jogo(mensagem)

    def processo_adicao_saldo(self, valor, forma_pagamento):
        sucesso, mensagem = self.saldo_model.add_saldo(valor)
        if sucesso:
            mensagem_completa = f"{mensagem} via {forma_pagamento}"
            self.view.sucesso_adicao_saldo(mensagem_completa)
            self.ir_inicio
        else:
            self.view.erro_adicao_jogo(mensagem)

    def processo_adicao_carrinho(self, jogo):
        self.carrinho_model.add_produto(jogo)
        self.view.sucesso_adicao_carrinho(jogo['nome'])

    def processo_remocao_produto(self, jogo):
        self.carrinho_model.remover(jogo)
        self.ir_carrinho()

    def processo_finalizacao_compra(self):
        sucesso, mensagem = self.compra_model.finalizar_compra()
        if sucesso:
            self.view_sucesso_compra(mensagem)
            self.ir_carrinho()
        else:
            self.view.erro_compra(mensagem)

    def fechar_app(self):
        self.view.fechar_app()

