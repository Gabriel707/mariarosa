from models.cliente import Cliente
from models.kit import *
from models.itens.macaquinho import Macaquinho
from models.itens import *


cliente_1 = Cliente('Gabriel', 'Gold')

compra_1 = Kit(cliente_1._nome, 39.90, 'Macaquinho Ursinho')

macaquinho_1 = Macaquinho('Joaninha', 49.90, '100% algodão')

compra_1.adicionar_no_carrinho(macaquinho_1)


def main():
    compra_1.exibir_itens_carrinho


if __name__ == '__main__':
    main()
