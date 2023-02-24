from contacorrente import ContaCorrente


class ContaEspecial(ContaCorrente):
    def __init__(self, cli, sal,limite):
        super().__init__(cli, sal)
        self._limite = limite
    def sacar(self,valor):
        if self._saldo + self._limite >= valor:
            if self._saldo >= valor:
                self._saldo -= valor
            else:
                resto = valor - self._saldo
                self._saldo = 0
                self._limite -= resto
        else:
            print("Saldo insuficiente")

    def __str__(self):
        return f"Conta Especial: {self._numero}, Titular: {self._titular}, Saldo: R${self._saldo}, Limite: R${self._limite}"

