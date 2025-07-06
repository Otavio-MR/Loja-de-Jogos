# Gerencia o saldo do usuario
class Saldo:
    def __init__(self, valor_inicial):
        self.saldo = valor_inicial

    # Adiciona um valor ao saldo
    def add_saldo(self, valor):
        self.saldo += valor

    # Tenta descontar um valor
    def desconto_saldo(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            return True
        else:
            return False # Se caso o saldo for insuficiente

    # Retorna o saldo atual
    def get_saldo(self):
        return self.saldo