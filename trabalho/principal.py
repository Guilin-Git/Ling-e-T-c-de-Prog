import produto
import vendas
import random
import os
import matplotlib.pyplot as plt



def salvar_dados_txt(lista_produtos, lista_vendas, faturamento_total):
    with open("dados_vendas.txt", "w") as arquivo:
        arquivo.write(f"Faturamento Total: R${faturamento_total:.2f}\n")
        arquivo.write("Detalhes de Vendas:\n")
        for venda in lista_vendas:
            arquivo.write(f"{venda.quantidade} - Produto(ID: {venda.produto.id}, Preço: R${venda.produto.preco:.2f})\n")

def carregar_dados_txt():
    lista_produtos = []
    lista_vendas = []
    faturamento_total = 0.0

    if os.path.exists("dados_vendas.txt") and os.path.getsize("dados_vendas.txt") > 0:
        with open("dados_vendas.txt", "r") as arquivo:
            linhas = arquivo.readlines()
            faturamento_str = linhas[0].split()[-1]
            faturamento_total = float(faturamento_str.replace("R$", "").replace(",", ""))
            detalhes_vendas = linhas[2:]
            for detalhe in detalhes_vendas:
                if " - Produto(ID: " in detalhe:
                    partes = detalhe.strip().split(" - ")
                    quantidade = int(partes[0])
                    produto_info = partes[1]
                    preco_produto = float(produto_info.split("Preço: R$")[1].split(")")[0].replace(",", ""))
                    id_produto = int(produto_info.split("Produto(ID: ")[1].split(",")[0])
                    novo_produto = produto.Produto(id_produto, preco_produto)
                    venda = vendas.Vendas(quantidade, novo_produto)
                    lista_vendas.append(venda)

    return lista_produtos, lista_vendas, faturamento_total

def calcular_faturamento(lista_vendas):
    return sum(venda.faturamento() for venda in lista_vendas)

def imprimir_faturamento_detalhado(lista_vendas):
    for venda in lista_vendas:
        print(f"{venda} - Faturamento: R${venda.faturamento():.2f}")

def calcular_percentuais_vendas(lista_vendas, faturamento_total):
    faturamentos_individuais = [venda.faturamento() for venda in lista_vendas]
    percentuais = [(faturamento / faturamento_total) * 100 for faturamento in faturamentos_individuais]
    return percentuais

def main():
    lista_produtos, lista_vendas, faturamento_total = carregar_dados_txt()

    if not lista_vendas:
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

        faturamento_total = calcular_faturamento(lista_vendas)
        print("Novos valores gerados.")

    while True:
        print("\nMenu:")
        print("1. Cálculo do faturamento")
        print("2. Impressão do faturamento detalhado")
        print("3. Cálculo de percentuais de vendas")
        print("4. Gravar os dados das vendas em um arquivo txt")
        print("5. Imprimir gráfico de vendas para as cinco mercadorias mais vendidas")
        print("6. Sair")

        escolha = input("Escolha a opção: ")

        if escolha == "1":
            faturamento_total = calcular_faturamento(lista_vendas)
            print(f"Faturamento Total: R${faturamento_total:.2f}")
        elif escolha == "2":
            imprimir_faturamento_detalhado(lista_vendas)
        elif escolha == "3":
            percentuais = calcular_percentuais_vendas(lista_vendas, faturamento_total)
            for i, venda in enumerate(lista_vendas):
                print(f"{venda} - Percentual: {percentuais[i]:.2f}%")
        elif escolha == "4":
            salvar_dados_txt(lista_produtos, lista_vendas, faturamento_total)
            print("Dados salvos em 'dados_vendas.txt'")
        elif escolha == "5":
            # Gráfico das cinco mercadorias mais vendidas
            top5_vendas = sorted(lista_vendas, key=lambda venda: venda.quantidade, reverse=True)[:5]
            mercadorias = [venda.produto.id for venda in top5_vendas]
            quantidades = [venda.quantidade for venda in top5_vendas]

            plt.bar(mercadorias, quantidades)
            plt.xlabel('Mercadorias')
            plt.ylabel('Quantidades Vendidas')
            plt.title('Top 5 Mercadorias Mais Vendidas')
            plt.xticks(mercadorias)
            plt.show()
        elif escolha == "6":
            break
        else:
            print("Opção inválida. Escolha uma opção válida.")

if __name__ == "__main__":
    main()
