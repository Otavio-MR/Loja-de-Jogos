# Representa o carrinho com os jogos adicionados
class Carrinho:
    def __init__(self):
        self.produtos = [] # Lista de dicionários (nome, preço, quantidade)

    # Adiciona um jogo ao carrinho (aumenta a quantidade se já existir)
    def add_produto(self, jogo):
        for produto in self.produtos:
            if produto["nome"] == jogo["nome"]:
                produto["quantidade"] += 1
                return
        # Se caso for novo, adiciona ao carrinho
        self.produtos.append({"nome": jogo["nome"], "preco": jogo["preco"], "quantidade": 1})

    # Remove uma unidade de jogo (Ou remove completamente, se caso houver apenas um)
    def remover(self, jogo):
        for produto in self.produtos:
            if produto["nome"] == jogo["nome"]:
                if produto["quantidade"] > 1:
                    produto["quantidade"] -= 1
                else:
                    self.produtos.remove(produto)
                break

    # Faz o calcúlo total da compra
    def calculo_total(self):
        return sum(produto["preco"] * produto["quantidade"] for produto in self.produtos)

    # Limpa o carrinho
    def limpar(self):
        self.produtos = []