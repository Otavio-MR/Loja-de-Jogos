from pymongo import MongoClient

# Classe que gerencia a conexão com o MongoDB
class Mongo:
    def __init__(self):
        try:
            # Conecta ao servidor do DB
            self.cliente = MongoClient("mongodb+srv://Otavio:123admin123@lojadejogos.rvox2pj.mongodb.net/?retryWrites=true&w=majority&appName=LojaDeJogos")
            self.mongo = self.cliente["LojaDeJogos"]

            # Define as coleções
            self.jogos = self.mongo["jogos"]
            self.historico = self.mongo["historico"]
            self.saldo = self.mongo["saldo"]

            # Teste da conexão
            print("✅ Conexão com o MongoDB Atlas feita com sucesso!")
        except Exception as e:
            print(f"Erro ao conectar ao MongoDB: {e}")

    # Insere um novo jogo a coleção
    def salvar_jogos(self, jogo_dic):
        self.jogos.insert_one(jogo_dic)

    # Lista todos os jogos cadastrados
    def lista_jogos(self):
        return list(self.jogos.find())

    # Salva uma compra no histórico
    def salvar_compra(self, compra_dic):
        try:
            self.historico.insert_one(compra_dic)
            print("Compra Salva no Historico")
        except Exception as e:
            print(f"Erro ao salvar no Historico: {e}")

    # Lista o histórico de compras
    def lista_historico(self):
        return list(self.historico.find())

    # Salva o saldo atual
    def salvar_saldo(self, saldo):
        try:
            self.saldo.delete_many({}) # Limpa o saldo antigo
            self.saldo.insert_one({"saldo": saldo})
            print("Saldo Atualizado com sucesso!")
        except Exception as e:
            print(f"Erro ao salvar no MongoDB: {e}")

    # Carrega o saldo atual
    def carregar_saldo(self):
        try:
            dado = self.saldo.find_one()
            if dado:
                return dado["saldo"]
            else:
                return 0.0
        except Exception as e:
            print(f"Erro ao carregar saldo do Mongo: {e}")
            return 0.0
