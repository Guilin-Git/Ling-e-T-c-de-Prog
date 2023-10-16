class Produto:
    def __init__(self, id, preco):
        self.id = id
        self.preco = preco

    def __str__(self):
        return f"Produto(ID: {self.id}, Preço: R${self.preco:.2f})"