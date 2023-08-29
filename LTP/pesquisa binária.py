# pesquisa binária

def buscabin(l, x, ini, fim):
    if ini > fim:
        return -1
    meio = (ini + fim) // 2
    if x == l[meio]:
        return meio
    elif x < l[meio]:
        return buscabin(l, x, ini, meio - 1)
    else:
        return buscabin(l, x, meio + 1, fim)

l = []

for i in range(100, 200):
    l.append(i)
print(l)

print("=" * 20)
print("inicio do programa")
print("=" * 20)

while True:
    y = input("Deseja procurar algum numero da lista? s/n: ")
    
    if y == "n":
        print("Obrigado por usar o nosso programa!")
        break
    elif y == "s":
        x = int(input("Digite um valor para pesquisa na lista: "))
        pos = buscabin(l, x, 0, len(l) - 1)
        if pos != -1:
            print("{0} está na posição {1} da lista".format(x, pos))
        else:
            print('{0} não está na lista'.format(x))
    else:
        print("Opção inválida. Digite 's' para continuar ou 'n' para sair.")

print("F I M")