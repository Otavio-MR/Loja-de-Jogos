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

    # Função para adicionar um novo jogo ao banco
    def adicionar_jogo(self, nome, genero, preco):
        return self.jogo_model.criar_jogo(nome, genero, preco)

    def finalizar_carrinho(self):
       return self.compra_model.finalizar_compra()

    def adicao_saldo(self, valor, forma_pagamento):
        sucesso, mensagem = self.saldo_model.add_saldo(valor)
        if sucesso:
            return True, f"{mensagem} via {forma_pagamento}"
        return False, mensagem

    def adicao_carrinho(self, jogo):
        self.carrinho_model.add_produto(jogo)
        return True, f"Jogo '{jogo['nome']}' adicionado com sucesso!"

    # Remove uma unidade de jogo no carrinho
    def remover_produto(self, jogo):
        self.carrinho_model.remover(jogo)
        return True, f"Jogo '{jogo['nome']}' removido com sucesso!"

    def obter_dados_carrinho(self):
        return {
            'produtos': self.carrinho_model.produtos,
            'total': self.carrinho_model.calculo_total()
        }

    def obter_saldo(self):
        return self.saldo_model.get_saldo()

    def fechar_app(self):
        self.view.fechar_app()

