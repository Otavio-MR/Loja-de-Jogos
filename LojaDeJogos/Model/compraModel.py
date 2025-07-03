from datetime import datetime

# Representa uma compra completa com as informações necessárias
class Compra:
    def __init__(self, jogos, total, data=None):
        self.jogos = jogos
        self.total = total
        self.data = data or datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    # Converte os dados da compra em um dicionário
    def para_dic(self):
        return {
            "jogos": self.jogos,
            "total": self.total,
            "data": self.data,
        }

    # Converte um dicionário em dados da compra
    @staticmethod
    def do_dic(data):
        return Compra(
            jogos=data["jogos"],
            total=data["total"],
            data=data["data"],
        )