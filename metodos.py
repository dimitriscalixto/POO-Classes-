class Pessoa:
    ano = 2023 # atributo de classe

    def __init__(self,nome, idade):
        self.nome = nome
        self.idade = idade
    @classmethod # possa chamar a classe sem chamar self, método da classe
    def metodo_de_clase(cls):
        print('hey')

    @classmethod  # possa chamar a classe sem chamar self, método da classe
    def criar_com_50_anos(cls,nome):
        return cls(nome, 50)


# p1 = Pessoa('Diogenes', 299)
p2 = Pessoa.criar_com_50_anos('Flavio')
print(p2.nome)
print(p2.idade)