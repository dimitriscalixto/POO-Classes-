from jogador import Jogador


class Zagueiro(Jogador):
    def __init__(self, nome, idade):
        super().__init__(nome, idade, "zagueiro")

    def desarmar(self):
        print(f"{self.nome} desarmou o atacante")
