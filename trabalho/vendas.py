class Vendas:
    def __init__(self, quantidade, produto):
        self.quantidade = quantidade
        self.produto = produto

    def faturamento(self):
        return self.quantidade * self.produto.preco    

    def __str__(self):
        return f"Quantidade vendida: {self.quantidade} Produto: {self.produto}"