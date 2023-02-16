from produtos import Produto

class ProdutoParcelado(Produto):

    def __init__(self, nome='', preco_compra=0, quantidade_estoque=0):
        super().__init__(nome, preco_compra, quantidade_estoque)

    def define_preco_venda(self, num):
        self._preco_venda = super().define_preco_venda(num) + self._preco_venda * 0.05