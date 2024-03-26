from models.itens.item_geral import ItemGeral


class Macaquinho(ItemGeral):
    def __init__(self, nome, preco, descricao, cor):
        super().__init__(nome, preco)
        self.descricao = descricao

    def __str__(self):
        return self._nome
