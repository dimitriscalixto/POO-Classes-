class Animal:
    # nome = 'Leão'

    def __init__(self, nome):
        self.nome = nome

        variavel = 'valor'
        print(variavel)

    def acao(self, alimento):
        print(variavel)  # não consigo acessar variavel dentro de acao
        print(f'{self.nome} está comendo {alimento} ')


leao = Animal('Leão')
print(leao.nome)
leao.acao('maçã')
