import os
import numpy as np

class Funcionario:
    def __init__(self, nome, cargo, salario, horas_trabalhadas):
        self.nome = nome
        self.cargo = cargo
        self.salario = salario
        self.horas_trabalhadas = horas_trabalhadas

    def __str__(self):
        return f"Nome: {self.nome}\nCargo: {self.cargo}\nSalário: {self.salario}\nHoras Trabalhadas: {self.horas_trabalhadas}"

def Escrever_arquivos():
    funcionarios = []

    if not os.path.exists("folha_pag.csv"):
        open("folha_pag.csv", "w").close()  # Cria o arquivo se ele não existe

    with open("folha_pag.csv", "r") as arquivo:
        linhas = arquivo.readlines()
        nomes_registrados = [linha.strip().split(": ")[1] for i, linha in enumerate(linhas) if i % 4 == 0]

    while True:
        nome = str(input("Digite o nome do funcionário: "))

        if nome in nomes_registrados:
            print(f"O funcionário {nome} já está registrado.")
        else:
            cargo = input("Digite o cargo do funcionário: ")
            while any(char.isdigit() for char in cargo):
                print("Cargo inválido. Digite novamente.")
                cargo = input("Digite o cargo do funcionário: ")

            while True:
                salario_input = input("Digite o salário do funcionário: ")
                if salario_input.isdigit():
                    salario = int(salario_input)
                    break
                else:
                    print("Salário inválido. Digite novamente.")

            horas_trabalhadas = str(input("Digite quantas horas trabalhadas tem esse funcionário: "))

            funcionario = Funcionario(nome, cargo, salario, horas_trabalhadas)
            funcionarios.append(funcionario)
            nomes_registrados.append(nome)  # Adicione o nome à lista de nomes registrados

        y = str(input("Continuar (s/n)? "))
        if y != "s":
            break

    with open("folha_pag.csv", "a") as arquivo:
        for funcionario in funcionarios:
            arquivo.write(str(funcionario) + "\n")

def imprimir_cadastro_funcionarios():
    try:
        with open("folha_pag.csv", "r") as arquivo:
            linhas = arquivo.readlines()

        for i in range(0, len(linhas), 4):
            nome = linhas[i].strip().split(": ")[1]
            cargo = linhas[i + 1].strip().split(": ")[1]
            salario = linhas[i + 2].strip().split(": ")[1]
            horas_trabalhadas = linhas[i + 3].strip().split(": ")[1]

            print("\n""|-----------------------------------------|")
            print("|Cadastro do Funcionário:")
            print(f"|Nome: {nome}")
            print(f"|Cargo: {cargo}")
            print(f"|Salário: {salario}")
            print(f"|Horas Trabalhadas: {horas_trabalhadas}")
            print("|-----------------------------------------|\n")

    except FileNotFoundError:
        print("O arquivo 'folha_pag.csv' não foi encontrado.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

def calcular_descontos_imposto():
    with open("folha_pag.csv", "r") as arquivo:
        linhas = arquivo.readlines()

    salarios = np.array([float(linhas[i + 2].strip().split(": ")[1]) for i in range(0, len(linhas), 4)])
    descontos = np.zeros_like(salarios)

    descontos[salarios <= 1500] = 0
    descontos[(salarios > 1500) & (salarios <= 3000)] = salarios[(salarios > 1500) & (salarios <= 3000)] * 0.15
    descontos[(salarios > 3000) & (salarios <= 5000)] = salarios[(salarios > 3000) & (salarios <= 5000)] * 0.20
    descontos[salarios > 5000] = salarios[salarios > 5000] * 0.27

    print("\nDescontos Calculados !!!!\n")       

def imprimir_relatorio():
    try:
        with open("folha_pag.csv", "r") as arquivo:
            linhas = arquivo.readlines()

        linhas = [linha.strip().split(": ")[1] for linha in linhas]
        salario = np.array([float(linhas[i]) for i in range(2, len(linhas), 4)])

        desconto = np.zeros_like(salario)
        desconto[salario <= 1500] = 0
        desconto[(salario > 1500) & (salario <= 3000)] = salario[(salario > 1500) & (salario <= 3000)] * 0.15
        desconto[(salario > 3000) & (salario <= 5000)] = salario[(salario > 3000) & (salario <= 5000)] * 0.20
        desconto[salario > 5000] = salario[salario > 5000] * 0.27

        total_desconto_ir = np.sum(desconto)
        total_salario_bruto = np.sum(salario)
        total_salario_liquido = total_salario_bruto - total_desconto_ir

        print("Relatório de Pagamento:")
        
        for i in range(0, len(linhas), 4):
            nome = linhas[i]
            salario_func = salario[i // 4]
            desconto_func = desconto[i // 4]
            salario_liquido = salario_func - desconto_func

            print(f"Funcionário: {nome}")
            print(f"Salário Bruto: R${salario_func:.2f}")
            print(f"Desconto de Imposto de Renda: R${desconto_func:.2f}")
            print(f"Salário Líquido: R${salario_liquido:.2f}")
            print("----")

        print(f"Total de Desconto de Imposto de Renda: R${total_desconto_ir:.2f}")
        print(f"Total de Salário Bruto: R${total_salario_bruto:.2f}")
        print(f"Total de Salário Líquido: R${total_salario_liquido:.2f}")

    except FileNotFoundError:
        print("O arquivo 'folha_pag.csv' não foi encontrado.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

def menu():
    while True:
        print("Menu:")
        print("1. Adicionar dados de funcionários")
        print("2. Listar cadastro de funcionários")
        print("3. Calcular descontos de imposto de renda")
        print("4. Imprimir relatório")
        print("5. Sair")
        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            Escrever_arquivos()
        elif escolha == "2":
            imprimir_cadastro_funcionarios()
        elif escolha == "3":
            calcular_descontos_imposto()
        elif escolha == "4":
            imprimir_relatorio()
        elif escolha == "5":
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()
