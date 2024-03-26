from models.cliente import Cliente
from models.produto import Produtos
from models.itens.macaquinho import Macaquinho
from models.itens.conjunto import Conjunto


compra_1 = Produtos('Macaquinho Florzinha', 39.90, 'M', 'Vermelho e branco')
compra_2 = Conjunto('Moletom Ursinho', 59.00, 'P',
                    'Conjunto Moletom 100% Algodão')

cliente_1 = Cliente('Gabriel', 'Gold')

compra_1.adicionar_macaquinho_para_carrinho(Macaquinho)


def main():
    print(compra_1)
    print(compra_2)


if __name__ == '__main__':
    main()
