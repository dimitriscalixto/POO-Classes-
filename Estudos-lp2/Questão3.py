from cliente import Cliente
from conta import Conta
from banco import Banco

cliente1 = Cliente('Dimitris', 'Rua dos bobos', '025.480.380-68', 19)
cliente2 = Cliente('Vitor', 'Hugo', '12309123123', 25)
conta1 = Conta(cliente1, 1000, 200)
conta2 = Conta(cliente2, 0, 1000)

print(conta1.numero)
print(conta2.numero)
