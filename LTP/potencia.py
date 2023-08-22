# funções de potencia e raiz quadrada usando biblioteca do python

import math

a = 3
b = 5

print(pow(a,b))
print(math.sqrt(9))

#função de potencia e raiz quadrada sem usar da biblioteca (manualmente)

def potencia():
    potencia = 0   
    x = int(input('Digite o primeiro valor que será elevado a "x" potencia : '))
    y = int(input('Digite o valor da potencia : '))

    for i in range (y):
        potencia = x*x
    print(f"A potencia de {x} elevado a {y} é igual a : " 2)
    return potencia

def Raiz():
    
    x = int(input('Digite o primeiro valor do qual sera tirado a raiz: '))
    y = int(input('Digite a ordem da raiz: '))
    z = 1/y

    Raiz = x  ** z



    print(f"A Raiz de ordem {y} de {x} é igual a : ")    
    return Raiz

       
    

    
print(potencia())

print(Raiz())