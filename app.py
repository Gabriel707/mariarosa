from models.cliente import Cliente
from models.produto import *
from models.itens.macaquinho import Macaquinho
from models.itens.conjunto import Conjunto
from models.itens import *


cliente_1 = Cliente('Gabriel', 'Gold')

compra_1 = Produtos('Macaquinho Florzinha', 39.90,
                        'M', 'Vermelho e branco')
compra_2 = Produtos('Conjuntinho Joaninha', 59.90, 'M', 'preto e branco')

compra_1.adicionar_no_carrinho()


def main():


if __name__ == '__main__':
    main()
