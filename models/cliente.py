from models.kit import Avaliacao_Kit


class Cliente():

    clientes = []

    def __init__(self, nome, categoria):
        self._nome = nome.title()
        self._categoria = categoria.upper()
        self._ativo = False
        self._avaliacao_produto = []
        Cliente.clientes.append(self)

    def __str__(self):
        return f'{self._nome} | {self._categoria}'

    @classmethod
    def listar_clientes(cls):
        print(f'{"CLIENTE".ljust(25)} | {
              'CATEGORIA'.ljust(25)} | {'STATUS\n'}')
        for cliente in cls.clientes:
            print(f'{cliente._nome.ljust(25)} | {
                  cliente._categoria.ljust(25)} | ATIVO {cliente.ativo}')

    @property
    def ativo(self):
        return '☑' if self._ativo else '☐'

    def alterar_estado(self):
        self._ativo = not self._ativo
