from models.itens.item_geral import ItemGeral


class Conjunto(ItemGeral):
    def __init__(self, nome, preco, tamanho, descricao):
        super().__init__(nome, preco)
        self.descricao = descricao

    def __str__(self):
        return self._nome
