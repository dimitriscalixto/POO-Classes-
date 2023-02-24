from conta import Conta


class Emprestimo:
    TAXA_JURO_MENSAL = 0.01  # taxa de juro mensal fixa
    emprestimos_realizados = 0  # contador de empréstimos realizados

    def __init__(self, valor, parcelas, juros, conta: Conta):
        self._parcelas = parcelas
        self._juros = juros
        self._conta = conta
        self._valor_total = valor
        self._valor_parcela = self._calcular_valor_parcela()
        self._parcelas_pagas = 0
        Emprestimo.emprestimos_realizados += 1

    def _calcular_valor_parcela(self):
        return self._valor_total / self._parcelas

    def pagar_mensalmente(self):
        if self._parcelas_pagas < self._parcelas:
            valor_a_pagar = self._valor_parcela + (self._valor_parcela * Emprestimo.TAXA_JURO_MENSAL)
            if self._conta._saldo >= valor_a_pagar:
                self._conta._saldo -= valor_a_pagar
                self._parcelas_pagas += 1
                if self._parcelas_pagas == self._parcelas:
                    sit = "Quitado"
                else:
                    sit = f"{self._parcelas_pagas} parcelas pagas de {self._parcelas}"
            else:
                sit = "Saldo insuficiente"
        else:
            sit = "Empréstimo já quitado"
        return sit

    def get_valor(self):
        return self._valor

    def set_valor(self, valor):
        self._valor = valor
        self._valor_total = self._calcular_valor_total()
        self._valor_parcela = self._calcular_valor_parcela()

    def get_parcelas(self):
        return self._parcelas

    def set_parcelas(self, parcelas):
        self._parcelas = parcelas
        self._valor_parcela = self._calcular_valor_parcela()

    def get_juros(self):
        return self._juros

    def set_juros(self, juros):
        self._juros = juros
        self._valor_total = self._calcular_valor_total()
        self._valor_parcela = self._calcular_valor_parcela()

    def get_conta(self):
        return self._conta

    def set_conta(self, conta):
        self._conta = conta

    def get_valor_total(self):
        return self._valor_total

    def get_valor_parcela(self):
        return self._valor_parcela

    def get_parcelas_pagas(self):
        return self._parcelas_pagas

    def set_parcelas_pagas(self, parcelas_pagas):
        self._parcelas_pagas = parcelas_pagas
