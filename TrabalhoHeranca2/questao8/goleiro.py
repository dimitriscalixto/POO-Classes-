from jogador import Jogador

class Goleiro(Jogador):
    def __init__(self, nome, idade):
        super().__init__(nome, idade, "goleiro")

    def defender(self):
        print(f"{self.nome} defendeu a bola")
