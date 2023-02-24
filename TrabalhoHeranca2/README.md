# Lista Sobre Herança 2.0 - Individual
### A partir do exemplo do sistema bancário, considere as seguintes classes.
``` Python
class Banco:
def __init__(self, numero, nome):
self._num = num
self._nome = nome
self._listaContas = []
//Métodos
```
``` Python
class Conta:
def __init__(self, n, cli, sal):
self._numero = n
self._titular = cli
self._saldo = sal
//Métodos
```

1. Adicione na classe conta um método chamado `atualiza()` para atualizar a conta de acordo
com uma taxa percentual.

2. Crie duas subclasses da classe Conta: `ContaCorrente` e `ContaPoupanca`. Ambas terão o
método `atualiza()` reescrito: a `ContaCorrente` deve atualizar-se com o dobro da taxa e a
`ContaPoupanca` deve atualizar-se com o triplo da taxa. Além disso, a ContaCorrente deve
reescrever o método `depositar()` a fim de retirar uma taxa bancária de dez centavos de cada
depósito.

3. Implemente a classe `ContaEspecial` herdando da classe `ContaCorrente`. Os objetos
dessa classe possuem um limite de crédito. Dessa forma, podem fazer saques até esse valor
limite, mesmo que não possuam saldo suficiente na conta. O construtor da classe
`ContaEspecial` deve receber como parâmetro, além dos parâmetros da superclasse, o limite
que o banco disponibiliza para o cliente. Sobrescreva o método sacar na classe ContaEspecial, de modo que o cliente possa ficar com saldo negativo até o valor de seu limite.

5. Crie um método `atualizar_contas()` na classe Banco que seja responsável por controlar a
atualização de todas as contas bancárias e gere um relatório com o saldo anterior e saldo novo
de cada uma das contas e o saldo total de todas as atualizações. 

5. Se você precisasse criar uma classe `ContaInvestimento`, você precisaria alterar o método
`atualizar_contas()`? Por que?

6. Sobrescreva o método `__str__()` na classe Conta. Faça com que ele retorne um resumo das
contas com o nome do titular e o saldo.

7. E se criarmos uma classe que não é filha de Conta e tentar passar uma instância no método
`atualizar_contas()`, o que acontece?
8. Crie um modelo de herança com, no mínimo, 3 classes para exemplificar o uso do conceito de
polimorfismo.