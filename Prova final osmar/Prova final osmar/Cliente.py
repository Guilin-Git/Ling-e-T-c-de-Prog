import pandas
class Cliente:
    def __init__(self, CPF, nome):
        self.CPF = CPF
        self.nome = nome

    def salvar_arquivo(self):
        with open("dados_clientes.csv", "a") as arquivo:
            arquivo.write("___________________________________\n")
            arquivo.write(f"| CPF do cliente: {self.CPF}     \n")
            arquivo.write(f"| Nome do cliente: {self.nome}   \n")
            arquivo.write("___________________________________\n")
            
    @classmethod

    def Cadastro_Cliente(cls):
        nome = input("Digite o Nome do cliente : ")
        while True:
            CPF = input("Digite o CPF do cliente : ")
            if len(CPF) == 11 and CPF.isdigit():
                break
            else:
                print("O CPF deve conter 11 digitos numéricos. Digite Novamente")
        novo_cliente = cls(CPF,nome)
        novo_cliente.salvar_arquivo()

    @classmethod

    def Imprimir_cadastro(cls):
        with open("dados_clientes.csv", "r") as arquivo:
            linhas = arquivo.readlines()
            for linha in linhas:
                print (linha)

