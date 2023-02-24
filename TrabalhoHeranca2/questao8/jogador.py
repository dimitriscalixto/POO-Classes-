class Jogador:
    def __init__(self, nome, idade, posicao):
        self.nome = nome
        self.idade = idade
        self.posicao = posicao
        self.habilidade = 0

    def definir_habilidade(self, habilidade):
        self.habilidade = habilidade

    def jogar(self):
        print(f"{self.nome} está jogando na posição {self.posicao}")
