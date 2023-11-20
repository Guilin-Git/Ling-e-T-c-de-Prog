import pandas
class Cliente:
    def __init__(self, CPF, nome):
        self.CPF = CPF
        self.nome = nome

    def salvar_arquivo(self):
        with open("dados_clientes.csv", "a") as arquivo:
            arquivo.write(f"Nome do cliente: {self.nome} | CPF do cliente: {self.CPF}\n")

    @classmethod

    def Cadastro_Cliente(cls):
        nome = input("Digite o Nome do cliente : ")
        CPF = input("Digite o CPF do cliente : ")
        novo_cliente = cls(CPF,nome)
        novo_cliente.salvar_arquivo()

    @classmethod

    def Imprimir_cadastro(cls):
        with open("dados_clientes.csv", "r") as arquivo:
            linhas = arquivo.readlines()
            for linha in linhas:
                print (linha)

Cliente.Cadastro_Cliente()
Cliente.Imprimir_cadastro()
