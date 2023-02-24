from jogador import Jogador


class Atacante(Jogador):
    def __init__(self, nome, idade):
        super().__init__(nome, idade, "atacante")

    def finalizar(self):
        print(f"{self.nome} finalizou a bola")
