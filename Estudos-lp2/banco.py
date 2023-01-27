from conta import Conta


class Banco:
    __slots__ = ['_num', '_nome', '_contas']

    def __init__(self, num, nome):
        self._num = num
        self._nome = nome
        self._contas = []

    def adicionar(self, conta):
        self._contas.append(conta)

    def remover(self, num):
        for conta in self._contas:
            if conta._numero == num:
                self._contas.remove(conta)

    def listar(self):
        total_banco = 0
        for conta in self._contas:
            total_banco += conta._saldo
            print(
                f'Titular:{conta._titular._nome} | Conta:{conta._numero} | Saldo:{conta._saldo} | Extrato: {conta._historico.imprime()}')
        print(f'Saldo total do banco é: {total_banco}')
