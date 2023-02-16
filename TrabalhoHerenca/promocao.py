from produtos import Produto


class Promocao(Produto):

    def __init__(self, nome='', preco_compra=0, quantidade_estoque=0):
        super().__init__(nome, preco_compra, quantidade_estoque)

    def define_preco_venda(self, num):
        self._preco_venda = super().define_preco_venda(num) - self._preco_venda * 0.5

    def vender_produto(self, num):
        if self._quantidade_estoque >= num:
            self._quantidade_estoque -= num
            self._historico.transacoes.append(f'Venda do produto na promoção no valor de: {self._preco_venda * num}')
        else:
            print("Não há estoque desse produto")

