from historico import Historico


class Conta:
    n_conta = 0
    __slots__ = ['_numero', '_titular', '_saldo', '_limite', '_historico', '_bloqueada']

    def __init__(self, cli, sal, lim, bloq=False):
        Conta.n_conta += 1
        self._numero = Conta.n_conta
        self._titular = cli
        self._saldo = sal
        self._limite = lim
        self._bloqueada = bloq
        self._historico = Historico()

    @property  # Método getter
    def numero(self):
        return self._numero

    def bloqueia_conta(self):
        if self._saldo == 0:
            print('conta bloqueada com sucesso')
            self._bloqueada = True
        else:
            print('conta tem saldo, não tem como bloquear')

    def sacar(self, valor):
        if self._bloqueada == True:
            return 'Saque não pode ser efetuado, conta bloqueada'
        else:
            if self._saldo < valor:
                return False
            else:
                self._saldo = self._saldo - valor
                self._historico.transacoes.append(f'Saque de {valor}')
                return True

    def depositar(self, valor):
        if self._bloqueada == True:
            return 'Deposito  não pode ser efetuado, conta bloqueada'
        else:
            self._saldo += valor
            self._historico.transacoes.append(f'Depósito de {valor}')

    def transfere(self, c_destino, valor):
        if self._bloqueada == True:
            return 'Transferência  não pode ser efetuada, conta bloqueada'
        else:
            self.sacar(valor)
            c_destino.depositar(valor)
            self._historico.transacoes.append(f'Tranferência de {valor}')

    def extrato(self):
        if self._bloqueada == True:
            return 'Extrato não pode ser consultado, conta bloqueada'
        else:
            self._historico.imprime()

    def __str__(self):
        return f'{self.__class__.__name__} {self._numero}: {self._titular} Saldo: {self._saldo}'
