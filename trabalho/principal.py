import produto
import vendas
import random
import os

# Função para salvar os dados em um arquivo de texto
def salvar_dados_txt(lista_produtos, lista_vendas, faturamento_total):
    with open("dados_vendas.txt", "w") as arquivo:
        arquivo.write(f"Faturamento Total: R${faturamento_total:.2f}\n")
        arquivo.write("Detalhes de Vendas:\n")
        for venda in lista_vendas:
            arquivo.write(f"{venda}\n")  # Escreva cada venda em uma linha separada

# Função para carregar os dados de um arquivo de texto
# Função para carregar os dados de um arquivo de texto
def carregar_dados_txt():
    lista_produtos = []
    lista_vendas = []
    faturamento_total = 0.0

    if os.path.exists("dados_vendas.txt"):
        with open("dados_vendas.txt", "r") as arquivo:
            linhas = arquivo.readlines()
            faturamento_str = linhas[0].split()[-1]  # Extrai a parte numérica do faturamento
            faturamento_total = float(faturamento_str.replace("R$", "").replace(",", ""))  # Remove "R$" e vírgulas
            detalhes_vendas = linhas[2:]
            for detalhe in detalhes_vendas:
                if "Quantidade vendida" in detalhe:
                    partes = detalhe.strip().split(" - ")
                    quantidade = str(partes[0].split(": ")[1])  # Correção aqui
                    produto_info = partes[1]
                    id_produto = int(produto_info.split("Produto(ID: ")[1].split(",")[0])
                    preco_produto = float(produto_info.split("Preço: R$")[1].replace(",", ""))
                    produto = produto.Produto(id_produto, preco_produto)
                    venda = vendas.Vendas(quantidade, produto)
                    lista_vendas.append(venda)

    return lista_produtos, lista_vendas, faturamento_total


# Carregando os dados existentes ou criando novos
lista_produtos, lista_vendas, faturamento_total = carregar_dados_txt()

if not lista_produtos:
    # Crie uma lista vazia para armazenar os produtos
    lista_produtos = []

    # Criar 100 produtos com IDs de 1 a 100 e preços aleatórios
    for i in range(1, 101):
        preco = round(random.uniform(1.0, 100.0), 2)  # Preço aleatório entre R$1,00 e R$100,00
        produto_novo = produto.Produto(i, preco)
        lista_produtos.append(produto_novo)

    lista_vendas = []    

    for i in range(0, 100):
        quantidadeVendida = random.randint(1, 50)  # quantidade de produto vendida aleatoriamente de 1 a 50 unidades
        venda_nova = vendas.Vendas(quantidadeVendida, lista_produtos[i])
        lista_vendas.append(venda_nova)

    # Calcule o faturamento total somando o faturamento de cada venda
    faturamento_total = sum(venda.faturamento() for venda in lista_vendas)

    salvar_dados_txt(lista_produtos, lista_vendas, faturamento_total)

# Calcule os faturamentos individuais e percentuais de vendas por mercadoria
faturamentos_individuais = [venda.faturamento() for venda in lista_vendas]
percentuais = [(faturamento / faturamento_total) * 100 for faturamento in faturamentos_individuais]

# Imprima os detalhes de cada venda e os percentuais
for i, venda in enumerate(lista_vendas):
    print(f"{venda} - Faturamento: R${venda.faturamento():.2f} - Percentual: {percentuais[i]:.2f}%")

# Imprima o faturamento total
print("\nFaturamento Total: R${:.2f}".format(faturamento_total))

# Salve os dados após a execução
salvar_dados_txt(lista_produtos, lista_vendas, faturamento_total)