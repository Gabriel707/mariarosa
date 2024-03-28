from models.cliente import Cliente
from models.kit import *
from models.itens.macaquinho import Macaquinho
from models.itens.cobertinha import Cobertinha
from models.itens import *


cliente_1 = Cliente('Gabriel', 'Gold')

kit_1 = Kit('Kit BabyBlackFriday', '100% antialergico')

kit_macaquinho = Macaquinho('Estampa de macaquinho', 69.90, 'G')
kit_cobertas = Cobertinha('Coberta teletubies', 89.90, 'Infantil')
kit_1.adicionar_no_carrinho(kit_macaquinho)
kit_1.adicionar_no_carrinho(kit_cobertas)


def main():
    kit_1.exibir_itens_carrinho


if __name__ == '__main__':
    main()
