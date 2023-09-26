#Função lambda
pot = lambda x,y :x **y

print ("x elevado a y e: ", pot(5,3))

n = [1,2,3,4,5,6,10,15]

cubo = list(map(lambda x: x**3,n))
print(cubo)

m = list(filter(lambda x: x > 3, n))
print(m)

soma = lambda x: x[0] + x[1] + x[2] + x[3]

print(soma(n))
