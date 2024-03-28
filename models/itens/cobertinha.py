from models.itens.item_geral import ItemGeral


class Cobertinha(ItemGeral):
    def __init__(self, nome, preco, descricao):
        super().__init__(nome, preco)
        self.descricao = descricao

    def __str__(self):
        return self._nome
