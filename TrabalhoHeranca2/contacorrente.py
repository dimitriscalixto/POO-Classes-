from conta import Conta

class ContaCorrente(Conta):
    def __init__(self, n, cli, sal):
        super().__init__(n, cli, sal)

    def atualiza(self):
        self._saldo -= self._saldo * 0.1
        return self._saldo