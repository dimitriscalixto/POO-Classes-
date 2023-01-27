from cliente import Cliente
from conta import Conta
from banco import Banco
from historico import  Historico
cliente1 = Cliente('Dimitris', 'Rua dos bobos', '025.480.380-68', 19)
conta1 = Conta(cliente1, 1000, 200)
conta1.depositar(10)
Banco1 = Banco(1001, 'Santander')
Banco1.adicionar(conta1)

cliente2 = Cliente('Dimi', 'Rua dos bobos', '025.480.380-68', 19)
conta2 = Conta(cliente2, 1000, 200)

conta1.transfere(conta2, 200)
Banco1.adicionar(conta2)
Banco1.listar()
