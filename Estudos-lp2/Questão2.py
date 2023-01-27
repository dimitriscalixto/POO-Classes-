from cliente import Cliente
from conta import Conta
from banco import Banco

cliente1 = Cliente('Dimitris', 'Rua dos bobos', '025.480.380-68', 19) # Cpf verdadeiro
print(cliente1.validaCPF())

cliente1 = Cliente('Dimitris', 'Rua dos bobos', '111.444.777-05.', 19) # Cpf falso
print(cliente1.validaCPF())