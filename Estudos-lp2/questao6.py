from cliente import Cliente
from conta import Conta
from banco import Banco

banco = Banco(1001, 'Santander')
banco.patrimonio = 10000
print(banco.patrimonio)
