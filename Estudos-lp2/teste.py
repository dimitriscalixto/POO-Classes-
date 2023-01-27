from cliente import Cliente
from conta import Conta
from banco import Banco

cliente1 = Cliente('Dimitris', 'Rua dos bobos', '025.480.380-68', 19)
cliente3 = Cliente('Vitor', 'Hugo', '12309123123',25)
conta3 = Conta(cliente3, 0, 1000)
conta1 = Conta(cliente1, 1000, 200)
conta1.depositar(1000)
conta1.depositar(500)
conta1.sacar(500)
cliente2 = Cliente('Gregori', 'Calixto', '99999999999', 19)
conta2 = Conta(cliente2, 500, 1000)
Banco1 = Banco(1001, "Banco inter")
Banco1.adicionar(conta1)
Banco1.adicionar(conta2)
Banco1.listar()
conta2.extrato()

