from models.itens.item_geral import ItemGeral


class Cobertinha(ItemGeral):
    def __init__(self, nome, preco, tamanho):
        super().__init__(nome, preco)
        self.tamanho = tamanho

    def __str__(self):
        return self._nome
