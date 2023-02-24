from conta import Conta

class ContaPoupanca(Conta):
    def __init__(self, n, cli, sal):
        super().__init__(n, cli, sal)

    def atualiza(self):
        self._saldo -= self._saldo * 0.15
        return self._saldo

    def depositar(self, valor):
        if self._bloqueada == True:
            return 'Deposito  não pode ser efetuado, conta bloqueada'
        else:
            self._saldo += valor - 0.10
            self._historico.transacoes.append(f'Depósito de {valor}')