from models.avaliacao_produto import Avaliacao_Produto
from models.itens.item_geral import ItemGeral


class Produtos():
    produtos = []

    def __init__(self, nome, preco, cor, tamanho):
        self._nome = nome
        self._preco = preco
        self._cor = cor
        self._tamanho = tamanho
        self._avaliacao_produto = []
        self._carrinho = []
        Produtos.produtos.append(self)

    def __str__(self):
        return f'{self._nome} | {self._preco}'

    @classmethod
    def listar_produtos(cls):
        print(f'{"Nome do produto".ljust(25)} | {
              'Preço'.ljust(25)} | {'Avaliacao'.ljust(25)} |{'COR\n'}')
        for produto in cls.produtos:
            print(f"{produto._nome.ljust(25)} | {
                produto._preco.ljust(25)} | {str(produto.media_avaliacoes).ljust(25)} |COR {produto._cor}")

    def receber_avaliacao(self, cliente, nota):
        if 0 < nota <= 5:
            avaliacao_produto = Avaliacao_Produto(cliente, nota)
            self._avaliacao_produto.append(avaliacao_produto)

    @property
    def media_avaliacoes(self):
        if not self._avaliacao_produto:
            return '-'
        soma_das_notas = sum(
            avaliacao_produto._nota for avaliacao_produto in self._avaliacao_produto)
        quantidade_de_notas = len(self._avaliacao_produto)
        media = round(soma_das_notas / quantidade_de_notas, 1)
        return media

    def adicionar_no_carrinho(self, item):
        if isinstance(item, ItemGeral):
            self._carrinho.append(item)

    @property
    def exibir_itens_carrinho(self):
        print(f'Cardapio do restaurante {self._nome}\n')
        for i, item in enumerate(self._carrinho, start=1):
            if hasattr(item, 'descricao'):
                mensagem_macaquinho = f'{i}. Nome: {item._nome} | Preço: R${
                    item._preco} | Descrição: {item._descricao} '
                print(mensagem_macaquinho)
            else:
                mensagem_conjunto = f'{i}. Nome: {item._nome} | Preço: R${
                    item._preco} | Descricao: {item._descricao} '
                print(mensagem_conjunto)
