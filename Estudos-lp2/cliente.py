import re


class Cliente:
    __slots__ = ['_nome', '_endereco', '_CPF', '_idade', ]

    def __init__(self, n, e, cpf, i):
        self._nome = n
        self._endereco = e
        self._CPF = cpf
        self._idade = i

    def validaCPF(self):
        cpf_novo = re.sub(r'[^\w\s]', '', self._CPF)
        cpf_novo = cpf_novo[0:9]
        mult_inicio = 10
        soma = 0
        for num in cpf_novo:
            soma += int(num) * mult_inicio
            mult_inicio -= 1
        div_int = soma % 11
        if div_int < 2:
            cpf_novo = cpf_novo + '0'
        else:
            resto = 11 - div_int
            cpf_novo = cpf_novo + str(resto)
        cpf_novo = re.sub(r'[^\w\s]', '', cpf_novo)
        mult_inicio1 = 11
        soma = 0
        for num in cpf_novo:
            soma += int(num) * mult_inicio1
            mult_inicio1 -= 1
        div_int = soma % 11
        if div_int < 2:
            cpf_novo = cpf_novo + '0'
        else:
            resto = 11 - div_int
            cpf_novo = cpf_novo + str(resto)
        return re.sub(r'[^\w\s]', '', self._CPF) == cpf_novo
