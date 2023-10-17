import produto
import vendas
import random
import os

def salvar_dados_txt(lista_produtos, lista_vendas, faturamento_total):
    with open("dados_vendas.txt", "w") as arquivo:
        arquivo.write(f"Faturamento Total: R${faturamento_total:.2f}\n")
        arquivo.write("Detalhes de Vendas:\n")
        for venda in lista_vendas:
            arquivo.write(f"{venda.quantidade} - {venda.produto}\n")

def carregar_dados_txt():
    lista_produtos = []
    lista_vendas = []
    faturamento_total = 0.0

    if os.path.exists("dados_vendas.txt"):
        with open("dados_vendas.txt", "r") as arquivo:
            linhas = arquivo.readlines()
            faturamento_str = linhas[0].split()[-1]
            faturamento_total = float(faturamento_str.replace("R$", "").replace(",", ""))
            detalhes_vendas = linhas[2:]
            for detalhe in detalhes_vendas:
                if "Quantidade vendida" in detalhe:
                    partes = detalhe.strip().split(" - ")
                    quantidade = int(partes[0])  # Altere para int
                    produto_info = partes[1]
                    id_produto = int(produto_info.split("Produto(ID: ")[1].split(",")[0])
                    preco_produto = float(produto_info.split("Preço: R$")[1].replace(",", ""))
                    produto = produto.Produto(id_produto, preco_produto)
                    venda = vendas.Vendas(quantidade, produto)
                    lista_vendas.append(venda)

    return lista_produtos, lista_vendas, faturamento_total

lista_produtos, lista_vendas, faturamento_total = carregar_dados_txt()
print("Valores carregados:")
print(f"Produtos: {len(lista_produtos)}")
print(f"Vendas: {len(lista_vendas)}")
print(f"Faturamento Total: R${faturamento_total:.2f}")

if not faturamento_total:
    print("Gerando novos valores...")
    lista_produtos = []
    for i in range(1, 101):
        preco = round(random.uniform(1.0, 100.0), 2)
        produto_novo = produto.Produto(i, preco)
        lista_produtos.append(produto_novo)

    lista_vendas = []
    for i in range(0, 100):
        quantidadeVendida = random.randint(1, 50)
        venda_nova = vendas.Vendas(quantidadeVendida, lista_produtos[i])
        lista_vendas.append(venda_nova)

    faturamento_total = sum(venda.faturamento() for venda in lista_vendas)
    print("Novos valores gerados.")

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