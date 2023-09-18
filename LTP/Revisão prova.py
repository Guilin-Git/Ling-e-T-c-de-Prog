import math

a = 3
b = 5

print(pow(a,b))
print(math.sqrt(9))

#função de potencia e raiz quadrada sem usar da biblioteca (manualmente)

minha_lista = []
dic = {}
def lista():
    while True:
        x = int(input("Digite um valor que sera adicionado na lista: "))
        y = str(input("Deseja continuar? (s/n) "))
        minha_lista.append(x)
        if y == "n":
            break
def invlista():
    tamanho = len(minha_lista)
    for i in range(tamanho//2):
        minha_lista[i], minha_lista[tamanho - i - 1] = minha_lista[tamanho - i - 1], minha_lista[i]
def produto():
    resultado = 1
    for i in minha_lista:
        resultado *= i
    return resultado
def imprimir():
    print(f" A lista invertida é {minha_lista}")
    invlista()
    print(f" A lista original é {minha_lista}")
    resultado = produto()
    print(f" O produto dos elementos da lista é: {resultado}")


def dicionario():
    while True:
        nome = input("Digite o nome do aluno: ")
        if nome in dic:
            print("Já existe o aluno", nome)
        else:
            nota = float(input("Digite a Nota deste aluno: "))
            dic[nome] = nota
            x = str(input("Deseja continuar? (s/n)"))
            if x == "n".lower():
                break
def imprimirdic():
    print(dic)
def atualizar():
    atualização = {}
    while True:
        nome = input("Digite o nome do aluno: ")
        if nome in dic:
            nota = float(input("Digite a nova nota deste aluno: "))
            atualização[nome] = nota
            dic.update(atualização)
            x = str(input("Deseja continuar? (s/n)"))
            if x == "n":
                break
        else:
            print("Aluno inexistente ☺")
def dicexistente():
    dicAnt = {"arroz": 15, "feijao" : 16, "suco" : 22}
    dicNovo = {"arroz": 15, "feijao" : 16, "suco" : 22}
    novo = {}
    print(f"O dicionario antigo é {dicAnt}")
    while True:
        item = input("Digite o item que mudou de preço:  ")
        if item in dicNovo:
            preço = int(input("Digite o novo preço: "))
            novo[item] = preço
            dicNovo.update(novo)
            x = str(input("Deseja continuar? (s/n)"))
            if x == "n":
                break
        else:
            print("Produto inexistente")


    print(f"O dicionario alterado é {dicNovo}")
def conjunto():
    conjuntoA = set()
    conjuntoB = set()
    while True:
        x = int(input("Digite um elemento que sera adicionado no conjunto A: "))
        conjuntoA.add(x)
        y = str(input("Deseja adicionar mais? (s/n)"))
        if y =="n":
            break
    while True:
        z = int(input("Agora digite o numero que deseja adicionar no conjunto B: "))
        conjuntoB.add(z)
        a = str(input("Deseja adicionar mais? (s/n)"))
        if a == "n":
            break
    intersecção = conjuntoA.intersection(conjuntoB)
    if intersecção:
        print(f"A intersecção entre os conjuntos é {intersecção}")
    else:
        print("Não existe intersecção")
opção = 0

while opção != 10:
    print("+=======================+\n");
    print("|     Menu de Opcoes    |\n");
    print("+=======================+\n");
    print("|  1 - Criar lista      |\n");
    print("|  2 - Inverter lista   |\n");
    print("|  3 - Produto da lista |\n");
    print("|  4 - Imprimir lista   |\n");
    print("|  5 - Criar dicionario |\n");
    print("|  6 - Imprimir dic.    |\n");
    print("|  7 - Atualizar dic.   |\n");
    print("|  8 - Dic pre-existente|\n");
    print("|  9 - Intersecção conj |\n");
    print("|  10 - Sair            |\n");
    print("+=======================+\n");
    opção = int(input("Digite uma opção: "))

    if opção == 1:
        lista()
    elif opção == 2:
        invlista()
    elif opção == 3:
        produto()
    elif opção == 4:
        imprimir()
    elif opção == 5:
        dicionario()
    elif opção == 6:
        imprimirdic()
    elif opção == 7:
        atualizar()
    elif opção == 8:
        dicexistente()
    elif opção == 9:
        conjunto()