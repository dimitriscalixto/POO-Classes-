from historico import Historico


class Produto():
    def __init__(self, nome='', preco_compra=0, quantidade_estoque=0):
        self._nome = nome
        self._preco_compra = preco_compra
        self._quantidade_estoque = quantidade_estoque
        self._preco_venda = 0
        self._historico = Historico()

    def define_preco_venda(self, num):
        self._preco_venda = num
        return self._preco_venda

    @property
    def get_historico(self):
        return self._historico.imprime()

    def vender_produto(self, num):
        if self._quantidade_estoque >= num:
            self._quantidade_estoque -= num
            self._historico.transacoes.append(f'Venda do produto no valor de: {self._preco_venda * num}')
        else:
            print("Não há estoque desse produto")

    def comprar_produto(self):
        self._quantidade_estoque += 1
        Historico().transacoes.append(f'Compra do produto no preço de: {self._preco_compra}')
