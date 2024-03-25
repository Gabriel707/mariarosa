from modelos.cliente import Cliente
from modelos.produto import Produtos


conjunto_body_01 = Produtos('Body Cachorrinho', '39.99', 'branco e bege', 'M')

cliente_1 = Cliente('Gabriel', 'Gold')
cliente_2 = Cliente('Andre', 'Platinum')
cliente_3 = Cliente('Rosane', 'Silver')


conjunto_body_01.receber_avaliacao(cliente_1._nome, 10)
conjunto_body_01.receber_avaliacao(cliente_2._nome, 7)
conjunto_body_01.receber_avaliacao(cliente_3._nome, 6)


def main():
    Cliente.listar_clientes()


if __name__ == '__main__':
    main()
