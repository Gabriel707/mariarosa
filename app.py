from models.cliente import Cliente
from models.produto import Produtos
from models.itens.macaquinho import Macaquinho
from models.itens.conjunto import Conjunto


macaquinho_1 = Macaquinho('Macaquinho Florzinha',
                          39.90, 'M', 'Vermelho e branco')
conjuntinho_1 = Conjunto('Moletom Ursinho', 59.00, 'P',
                         'Conjunto Moletom 100% Algodão', )

cliente_1 = Cliente('Gabriel', 'Gold')


def main():
    print(macaquinho_1)
    print(conjuntinho_1)


if __name__ == '__main__':
    main()
