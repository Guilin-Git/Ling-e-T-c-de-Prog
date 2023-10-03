print("---------------- MATRIZ ----------------")
m =[[1,2,3],
    [4,5,6],
    [7,8,9]]

print("\n",m[0],"\n",m[1],"\n",m[2],"\n")
print(m[1], "=", sum(m[1]))

def diagonal(m):
    p = 1
    print("\n""A diagonal é : ", "\n")
    for i in range(len(m[0])):
        for j in range(len(m[0])):
            if i == j:
                p = p * m[i][j]
                print(m[i][j],"\n") 

    return p

print("Produto da Diagonal é :", diagonal(m) )


def produto(m):
    p = int(input("digite por qual valordeseja multiplicar a matriz : "))
    resultado = []
    print(f"O produto da matriz por {p} é :")
    for i in range(len(m[0])):
        linha = []
        for j in range(len(m[0])):
                elemento = m[i][j] * p
                linha.append(elemento)
        resultado.append(linha)
    return resultado
print(produto(m)) 

def potencia(m):
    p = int(input("Digite por qual valor deseja elevar a matriz: "))
    resultado = []

    for i in range(len(m)):
        linha = []
        for j in range(len(m[i])):
            elemento = m[i][j] ** p
            linha.append(elemento)
        resultado.append(linha)

    return resultado
print(potencia(m)) 


