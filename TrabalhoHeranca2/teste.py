from conta import Conta
from banco import Banco
from contacorrente import ContaCorrente

C1 = Conta('Dimitris', 1000)
C2 = ContaCorrente('Dimitris2', 2000,1000)
b1 = Banco(1001, 'Bradesco')
b1.adicionar(C1)
b1.adicionar(C2)
b1.atualizar_contas()
