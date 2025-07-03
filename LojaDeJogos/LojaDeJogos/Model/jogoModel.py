class Jogo:
    # Representa um jogo individualmente
    def __init__(self, nome, genero, preco):
        self.nome = nome
        self.genero = genero
        self.preco = preco

    # Converte os objetos em um dicionário para poder salvar no banco
    def para_dic(self):
        return {'nome': self.nome, 'genero': self.genero, 'preco': self.preco}

    @staticmethod
    # Recria um objeto de um dicionário, depois de ler no banco
    def do_dic(data):
        return Jogo(data['nome'], data['genero'], data['preco'])