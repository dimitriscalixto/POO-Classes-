from produtos import Produto
from produtoPromocional import ProdutoPromocional
from produtoParcelado import ProdutoParcelado
from promocao import Promocao


p1 = Produto("Bola", 100, 10)
p1.define_preco_venda(200)
p1.vender_produto(5)
print(p1.get_historico)

pp1 = ProdutoPromocional('Carrinho de brinquedo',50, 10)
p1.define_preco_venda(100)
p1.vender_produto(4)

ppar = ProdutoParcelado('Carrinho de brinquedo',50, 10)
ppar.define_preco_venda(100)
ppar.vender_produto(4)

promo = Promocao("Carro",40,10)
promo.define_preco_venda(160)
promo.vender_produto(4)
print(promo.get_historico)
# p1.vender_produto(10)  erro
