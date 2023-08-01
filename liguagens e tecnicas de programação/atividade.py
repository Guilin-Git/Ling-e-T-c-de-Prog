#Exercicio 1 Calcular Max e Min de uma lista usando while
lst = [2,3,6,2,0,7,8]

Max = lst[0]
Min = lst[0]
i = 0
total = 0

while i < len(lst):
    if lst[i] > Max:
            Max = lst[i]
    elif lst[i] < Min:
            Min = lst[i]

    total = total + lst[i]
    i += 1       

print("tamanho da lista = " , len(lst))
print("Valor Maximo = ", Max)
print("Valor Minimo = ", Min)

#--------------------------------------------#

# Exercico 2 somatorio



print("O valor da soma do numeros da lista é :", total)    

# Exercicio 3 lista de frunta

lstFruta = ['banana' , 'uva', 'maracuja', 'morango', 'pera']

for i in range(len(lstFruta)):
    print('fruta: ', lstFruta[i])

#exercicio 4 quantas letras r's tem na lista

a = 'osmar'

lstNome = a * 5
contador = 0

for i in lstNome:
    if (i == 'r'):
        contador +=1

print('O numero de R na lista é :', contador )



