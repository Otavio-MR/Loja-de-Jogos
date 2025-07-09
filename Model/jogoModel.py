class Jogo:
    def __init__(self, mongo):
        self.mongo = mongo

    def criar_jogo(self, nome, genero, preco):
        if not nome or not genero or not preco:
            return False, "Campos obrigatórios vazios."

        try:
            preco_float = float(preco)
        except ValueError:
            return False, "Preço inválido."

        jogo = {
            "nome": nome,
            "genero": genero,
            "preco": preco_float
        }

        self.mongo.salvar_jogos(jogo)
        return True, "Jogo adicionado com sucesso."