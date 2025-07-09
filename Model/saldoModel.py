# Gerencia o saldo do usuario
class Saldo:
    def __init__(self, mongo, valor_inicial):
        self.mongo = mongo
        self.saldo = float(valor_inicial)

    # Adiciona um valor ao saldo
    def add_saldo(self, valor):
        try:
            valor = float(valor)
            if valor <= 0:
                return False, "O valor deve ser um valor maior que 0"
            self.saldo += valor
            self.mongo.salvar_saldo(self.saldo)
            return True, f"Saldo adicionado: R$ {valor:.2f}"
        except ValueError:
            return False, "Valor inválido. Use apenas números!"

    # Tenta descontar um valor
    def desconto_saldo(self, valor):
        try:
            valor = float(valor)
            if valor <= self.saldo:
                self.saldo -= valor
                self.mongo.salvar_saldo(self.saldo)
                return True
            return False
        except ValueError:
            return False

    # Retorna o saldo atual
    def get_saldo(self):
        return self.saldo