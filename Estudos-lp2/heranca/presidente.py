from funcionario import Funcionario


class Presidente(Funcionario):

    def get_bonifica(self):
        return self._salario + 500
