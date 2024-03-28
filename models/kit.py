from models.avaliacao_produto import Avaliacao_Kit
from models.itens.item_geral import ItemGeral


class Kit():
    kits = []

    def __init__(self, nome, descricao):
        self._nome = nome.title()
        self._descricao = descricao.upper()
        self._ativo = False
        self._avaliacao_kit = []
        self._carrinho = []
        Kit.kits.append(self)

    def __str__(self):
        return f'{self._nome} | {self.descricao}'

    @classmethod
    def listar_produtos(cls):
        print(f'{"Nome do produto".ljust(25)} | {
              'Preço'.ljust(25)} | {'Avaliacao'.ljust(25)} |{'COR\n'}')
        for kit in cls.kits:
            print(f"{kit._nome.ljust(25)} | {
                kit._preco.ljust(25)} | {str(kit.media_avaliacoes).ljust(25)} |COR {kit._cor}")

    def receber_avaliacao(self, cliente, nota):
        if 0 < nota <= 5:
            avaliacao_kit = Avaliacao_Kit(cliente, nota)
            self._avaliacao_kit.append(avaliacao_kit)

    @property
    def media_avaliacoes(self):
        if not self._avaliacao_kit:
            return '-'
        soma_das_notas = sum(
            avaliacao_kit._nota for avaliacao_kit in self._avaliacao_kit)
        quantidade_de_notas = len(self._avaliacao_kit)
        media = round(soma_das_notas / quantidade_de_notas, 1)
        return media

    def adicionar_no_carrinho(self, item):
        if isinstance(item, ItemGeral):
            self._carrinho.append(item)

    @property
    def exibir_itens_carrinho(self):
        print(f'Item do Kit {self._nome}\n')
        for i, item in enumerate(self._carrinho, start=1):
            mensagem = f'{i}. Nome:{item._nome} | Preço: R${item._preco}'
            print(mensagem)
