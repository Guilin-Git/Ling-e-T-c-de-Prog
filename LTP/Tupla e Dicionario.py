list = [1,2,3,4,5,6]
print(list)
tupla = ('jorge', 123, 4.5, [1,2,3,4,5])
print(tupla)

#remover a lista da tupla e somar seus valores
def ExtracaoLista(tupla):
    L1 = tupla[len(tupla)-1]
    print(L1)
    return L1

def somaElementos(L):

    soma = 0
    for i in L:
        soma += i
    return soma     



def imprimir():

    lista_extraida = ExtracaoLista(tupla)
    resultado = somaElementos(lista_extraida)

    print("A soma dos elementos da lista que está inserida na tupla é: ", resultado )
    


    
imprimir()
