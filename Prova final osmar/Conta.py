import pandas
import Cliente

class Conta:
    ultimo_numero_conta = 0

    def __init__(self, titular, nome_titular, saldo, limite):
        Conta.ultimo_numero_conta += 1
        self.numero = Conta.ultimo_numero_conta
        self.titular = titular
        self.nome_titular = nome_titular
        self.saldo = saldo
        self.limite = limite

    def salvar_arquivo(self):
        with open("dados_contas.csv", "a") as arquivo:
            arquivo.write("___________________________________\n")
            arquivo.write(f"| Nome do cliente: {self.nome_titular}   \n")
            arquivo.write(f"| CPF do cliente: {self.titular}     \n")
            arquivo.write(f"| CPF do Titular: {self.titular} \n")
            arquivo.write(f"| Numero da Conta: {self.numero} \n")
            arquivo.write(f"| Saldo da Conta: {self.saldo}   \n")
            arquivo.write(f"| Limite da conta {self.limite}  \n")
            arquivo.write("|__________________________________|\n")

    @staticmethod
    def verificar_cpf_existente(cpf):
        with open("dados_clientes.csv", "r") as arquivo:
            for linha in arquivo:
                if f"CPF do cliente: {cpf}" in linha:
                    return True
        return False

    @staticmethod
    def obter_nome_por_cpf(cpf):
        with open("dados_clientes.csv", "r") as arquivo:
            for linha in arquivo:
                if f"CPF do cliente: {cpf}" in linha:
                    while "Nome do cliente:" not in linha:
                        linha = next(arquivo)
                    return linha.split(":")[1].strip()
        return None

    @classmethod
    def Cadastro_Conta(cls):
        titular = input("Digite o CPF do Titular da Conta: ")
        if not cls.verificar_cpf_existente(titular):
            print("O CPF do titular não está cadastrado como Cliente. Crie um cadastro como cliente antes de criar uma conta.")
            return

        nome_titular = cls.obter_nome_por_cpf(titular)
        saldo = float(input("Digite o saldo inicial da conta: "))
        limite = float(input("Digite o limite da conta: "))

        nova_conta = cls(titular, nome_titular, saldo, limite)
        nova_conta.salvar_arquivo()
        print(f"Conta cadastrada com sucesso. Número da Conta: {nova_conta.numero}")


    @classmethod
    def fazer_saque(cls):
        numero_conta = int(input("Digite o número da conta para saque: "))
        valor_saque = float(input("Digite o valor a ser sacado: "))

        # Obter a conta do arquivo ou outro meio de armazenamento
        # (não está implementado aqui)

        # Verificar se a conta existe e realizar o saque
        # (não está implementado aqui)

        print("Saque realizado com sucesso.")
    
    @classmethod
    def imprimir_contas(cls):
        with open("dados_contas.csv", "r") as arquivo:
            linhas = arquivo.readlines()
            for linha in linhas:
                print(linha)    