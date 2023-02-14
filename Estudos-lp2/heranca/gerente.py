from funcionario import Funcionario


class Gerente(Funcionario):
    def __init__(self, senha, qtd_gerenciados, nome, cpf, salario):
        super().__init__(nome, cpf, salario)
        self._senha = senha
        self._qtd_gerenciados = qtd_gerenciados

    def autentica(self, senha):
        if self._senha == senha:
            return True
        else:
            return False

    # imaginando um contexto em que a bonificação do gerente
    # seja igual a do Funcionário, mas com uma adição de 1000, utilizamos o super() para reaproveitar o código
    def get_bonifica(self):
        return super().get_bonifica() + 1000
