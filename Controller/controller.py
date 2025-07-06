from Model.mongoModel import Mongo
from Model.carrinhoModel import Carrinho as CarrinhoModel
from Model.saldoModel import Saldo as SaldoModel
from Model.jogoModel import Jogo
from Model.compraModel import Compra

from View.inicioView import Inicio
from View.catalogoView import Catalogo
from View.carrinhoView import Carrinho as CarrinhoView
from View.adicaoJogoView import AdicaoJogo
from View.saldoView import Saldo as SaldoView
from View.historicoView import Historico

import tkinter as tk
from datetime import datetime

class Controller:
    def __init__(self, root):
        self.root = root
        self.mongo = Mongo() # Conexão com o MongoDB

        # Models
        self.carrinho_model = CarrinhoModel()
        self.saldo_model = SaldoModel(self.mongo.carregar_saldo()) # Carrega o saldo do MongoDB

        # Views
        self.inicio_view = Inicio(root, self)
        self.catalogo_view = Catalogo(root, self)
        self.carrinho_view = CarrinhoView(root, self)
        self.adicaoJogo_view = AdicaoJogo(root, self)
        self.saldo_view = SaldoView(root, self)
        self.historico_view = Historico(root, self)

        self.mostrar_inicio()

    # Esconde todas as telas
    def esconder_telas(self):
        self.inicio_view.esconder()
        self.catalogo_view.esconder()
        self.carrinho_view.esconder()
        self.adicaoJogo_view.esconder()
        self.saldo_view.esconder()
        self.historico_view.esconder()

    # Exibe a tela incial
    def mostrar_inicio(self):
        self.esconder_telas()
        self.inicio_view.mostrar()

    # Exibe a tela do catálogo com os jogos salvos no DB
    def mostrar_catalogo(self):
        self.esconder_telas()
        jogos = self.mongo.lista_jogos()
        self.catalogo_view.exibir_jogos(jogos)
        self.catalogo_view.mostrar()

    # Exibe a tela do carrinho com os jogos adicionados e o total
    def mostrar_carrinho(self):
        self.esconder_telas()
        total = self.carrinho_model.calculo_total()
        jogos_carrinho = self.carrinho_model.produtos
        self.carrinho_view.exibir_carrinho(jogos_carrinho, total)
        self.carrinho_view.mostrar()

    # Exibe a tela de adição de jogos
    def mostrar_adicao(self):
        self.esconder_telas()
        self.adicaoJogo_view.limpar_campo()
        self.adicaoJogo_view.mostrar()

    # Exibe a tela de saldo e atualiza o valor atual
    def mostrar_saldo(self):
        self.esconder_telas()
        saldo = self.saldo_model.get_saldo()
        self.saldo_view.atualizar(saldo)
        self.saldo_view.mostrar()

    # Exibe o histórico de compras
    def mostrar_historico(self):
        self.esconder_telas()
        historico = self.mongo.lista_historico()
        self.historico_view.exibir(historico)
        self.historico_view.mostrar()

    # Função para adicionar um novo jogo ao banco
    def adicionar_jogo(self, nome, genero, preco):
        try:
            preco = float(preco)
            novo_jogo = Jogo(nome, genero, preco)
            self.mongo.salvar_jogos(novo_jogo.para_dic())
            return True, "Jogo salvo com sucesso!"
        except ValueError:
            return False, "Preço Inválido!"

    # Finaliza a compra atual (Desconta saldo, Salva no histórico, limpa o carrinho)
    def finalizar_carrinho(self):
        total = self.carrinho_model.calculo_total()

        if total == 0:
            return False, "Nenhum jogo foi encontrado!"

        if not self.saldo_model.desconto_saldo(total):
            return False, "Saldo insuficiente!"

        # Prepara os dados para a compra
        compra_dic = {
                "data" : datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
                "jogos" : [],
                "total" : total
            }

        # Adiciona os jogos comprados
        for produto in self.carrinho_model.produtos:
            compra_dic["jogos"].append({
                "nome" : produto["nome"],
                "quantidade" : produto["quantidade"],
                "preco_unit": produto["preco"],
                "preco_total" : produto["preco"] * produto["quantidade"],
            })

        # Salva compra e saldo no banco
        self.mongo.salvar_compra(compra_dic)
        self.mongo.salvar_saldo(self.saldo_model.get_saldo())

        # Limpa o carrinho e volta para o início
        self.carrinho_model.limpar()
        return True, "Compra finalizada com sucesso!"

    # Adiciona um jogo ao carrinho (aumenta quantidade se já existir)
    def adicao_carrinho(self, jogo):
        self.carrinho_model.add_produto(jogo)
        return True, "Jogo '{jogo['nome']}' adicionado com sucesso!"

    # Remove uma unidade de jogo no carrinho
    def remover_produto(self, jogo):
        self.carrinho_model.remover(jogo)
        self.mostrar_carrinho()
        return True, f"Jogo '{jogo['nome']}' removido com sucesso!"

    # Adiciona saldo ao saldo atual e salva no banco
    def adicao_saldo(self, valor, forma_pagamento):
        try:
            valor = float(valor)
            self.saldo_model.add_saldo(valor)
            self.mongo.salvar_saldo(self.saldo_model.get_saldo())
            return True, f"Saldo adicionado: R$ {valor:.2f} via {forma_pagamento}"
        except ValueError:
            return False, "Valor de saldo Inválido!"

    # Volta para a tela inicial
    def voltar_inicio(self):
        self.mostrar_inicio()

    # (Alias) Exibe a tela inicial
    def exibir_inicio(self):
        self.mostrar_inicio()


