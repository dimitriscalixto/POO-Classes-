class Pessoa:
    def __init__(self, nome, sobrenome, idade):
        self.nome = nome
        self.sobrenome = sobrenome
        self.idade = idade


class Carro:
    def __init__(self, marca, nome, cor, ):
        self.marca = marca
        self.nome = nome
        self.cor = cor

    def acelerar(self):
        print(f'{self.nome} está acelerando')


p1 = Pessoa('Dimitris', 'Calixto', 19)
c1 = Carro('Fiat', 'Cronos', 'Preto')

c1.acelerar() # Cronos está acelerando
