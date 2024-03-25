from models.avaliacao_produto import Avaliacao_Produto


class Produtos():

    produtos = []

    def __init__(self, nome, preco, cor, tamanho):
        self._nome = nome
        self._preco = preco
        self._cor = cor
        self._tamanho = tamanho
        self._avaliacao_produto = []
        Produtos.produtos.append(self)

    def __str__(self):
        return f'{self._nome} | {self._preco}'

    @classmethod
    def listar_produtos(cls):
        print(f'{"NOME".ljust(25)} | {
              'PRECO'.ljust(25)} | {'Avaliacao'.ljust(25)} |{'COR\n'}')
        for produto in cls.produtos:
            print(f'{produto._nome.ljust(25)} | {
                  produto._preco.ljust(25)} | {produto.media_avaliacoes}|COR {produto._cor}')

    def receber_avaliacao(self, cliente, nota):
        avaliacao_produto = Avaliacao_Produto(cliente, nota)
        self._avaliacao_produto.append(avaliacao_produto)

    @property
    def media_avaliacoes(self):
        if not self._avaliacao_produto:
            return 0
        soma_das_notas = sum(
            avaliacao_produto._nota for avaliacao_produto in self._avaliacao_produto)
        quantidade_de_notas = len(self._avaliacao_produto)
        media = round(soma_das_notas / quantidade_de_notas, 1)
        return media
