nota = []
nome = []
#def lenotanome

def lenotanome():
        x = int(input('Digite a quantidade de aluno : '))    
        for i in range (x):
            print('aluno {}'.format(i))
            while True:  
                try:
                    n = float(input('Digite a nota do aluno : '))
                    break
                except:
                    print("A nota do aluno deve ser numérico") 
                    
            m = input('Digite o nome do Aluno : ')
            nota.append(n)
            nome.append(m)
        

# função que avalia e imprime o conceitos dos alunos

def avalianotas():
    for i in range(len(nome)):
        if nota [i] >= 9.0 and nota [i] <= 10:
            print('o aluno {} tem conceito A e nota {}'.format(nome[i],nota[i]))
        if nota[i] < 9.0 and nota[i] >= 8.0:
            print('o aluno {} tem conceito B e Nota {}'.format(nome[i],nota[i]))
        if nota[i] >= 7.0 and nota[i] < 8.0:
            print('o aluno {} tem conceito C e Nota {}'.format(nome[i],nota[i]))
        if nota[i] < 7.0 and nota[i] >= 0.0:
            print('o aluno {} tem conceito D- e Nota {}'.format(nome[i],nota[i]))   


print(' INICIO DO PROGRAMA ')
lenotanome()                       
print (' MEIO DO PROGRAMA ')
avalianotas()
print(' FIM DO PROGRAMA ')