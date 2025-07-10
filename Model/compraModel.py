from datetime import datetime

# Representa uma compra completa com as informações necessárias
class Compra:
    def __init__(self, mongo, carrinho_model, saldo_model):
        self.mongo = mongo
        self.carrinho_model = carrinho_model
        self.saldo_model = saldo_model

    def finalizar_compra(self):
        if not self.carrinho_model.produtos:
            return False, "Nenhum jogo no carrinho!"

        produtos = self.carrinho_model.produtos
        total = sum(p['preco'] * p['quantidade'] for p in produtos)

        if not self.saldo_model.desconto_saldo(total):
            return False, "Saldo insuficiente!"

        # Criação do dicionário da compra para salvar
        jogos_formatados = []
        for p in produtos:
            jogos_formatados.append({
                'nome': p['nome'],
                'quantidade': p['quantidade'],
                'preco_total': p['preco'] * p['quantidade']
            })

        compra = {
            "data": datetime.now().strftime("%d/%m/%Y %H:%M"),
            "total": total,
            "jogos": jogos_formatados
        }

        self.mongo.salvar_compra(compra)
        self.mongo.salvar_saldo(self.saldo_model.get_saldo())
        self.carrinho_model.limpar()

        return True, "Compra finalizada com sucesso!"
