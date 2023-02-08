from funcionario import Funcionario


class Gerente(Funcionario):
    def __init__(self, senha, qtd_gerenciados, nome, cpf, salario):
        super().__init__( nome, cpf, salario)
        self._senha = senha
        self._qtd_gerenciados = qtd_gerenciados


def autentica(self, senha):
    if self._senha == senha:
        return True
    else:
        return False
