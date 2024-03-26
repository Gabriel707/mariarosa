from models.cliente import Cliente
from models.produto import *
from models.itens.macaquinho import Macaquinho
from models.itens.conjunto import Conjunto
from models.itens import *


cliente_1 = Cliente('Gabriel', 'Gold')

compra_1 = Produtos(cliente_1._nome, 39.90)
compra_2 = Produtos('Conjuntinho Joaninha', 59.90, 'M', 'preto e branco')

macaquinho_1 = Macaquinho('Macaquinho de Joaninha', 89.90, '')

compra_1.adicionar_no_carrinho()


def main():


if __name__ == '__main__':
    main()
