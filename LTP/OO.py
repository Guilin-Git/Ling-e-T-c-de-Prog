class pessoa():
    nome = str(input("digite o nome que deseja salvar : "))
    idade = int(input("digite a idade :"))
    sexo = str(input("digite o sexo: "))
    salario = int(input("digite quanto a pessoa recebe de salário : "))


    def IR(p):
        return(p.salario*27)


    def imprimir(p):
        print("Nome: ",p.nome) 
        print("Idade : ",p.idade)
        print("Salário : ",p.salario)
        print("Sexo : ", p.sexo)
        print("IR: ",p.IR())

p = pessoa()
print(p.imprimir())
