notas = {'João': 9, 'Maria': 10, 'José': 4, 'Pedro': 8}

nome = input("Digite o nome do aluno: ")
nota = float(input("Digite a Nota deste aluno: "))
print("Antigo dicionário ----->", notas)

if nome in notas:
    print("Já existe o aluno", nome)
else:
    notas[nome] = nota

print("Novo Dicionário ----->", notas)