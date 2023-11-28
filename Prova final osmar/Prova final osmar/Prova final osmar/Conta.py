import pandas
from datetime import datetime
from Historico import Historico

class Conta:

    def __init__(self, titular, nome_titular, saldo, limite):
        self.numero = self.obter_proximo_numero_conta()
        self.titular = titular
        self.nome_titular = nome_titular
        self.saldo = saldo
        self.limite = limite
        self.data_criacao = datetime.now()
        self.historico = Historico(self.numero, self.data_criacao, "Cadastro", self.data_criacao)
        self.historico.salvar_arquivo()

    @staticmethod
    def obter_proximo_numero_conta():
        try:
            with open("ultimo_numero_conta.txt", "r") as arquivo:
                ultimo_numero_conta = int(arquivo.read())
        except FileNotFoundError:
            ultimo_numero_conta = 0

        proximo_numero_conta = ultimo_numero_conta + 1

        with open("ultimo_numero_conta.txt", "w") as arquivo:
            arquivo.write(str(proximo_numero_conta))

        return proximo_numero_conta

    @staticmethod
    def formatar_data_hora(data_hora):
        return data_hora.strftime("%d/%m/%Y %H:%M:%S")    

    def salvar_arquivo(self):
        with open("dados_contas.csv", "a") as arquivo:
            arquivo.write("___________________________________\n")
            arquivo.write(f"| Nome do cliente: {self.nome_titular}   \n")
            arquivo.write(f"| CPF do cliente: {self.titular}     \n")
            arquivo.write(f"| CPF do Titular: {self.titular} \n")
            arquivo.write(f"| Numero da Conta: {self.numero} \n")
            arquivo.write(f"| Saldo da Conta: {self.saldo}   \n")
            arquivo.write(f"| Limite da conta: {self.limite}  \n")
            arquivo.write(f"| Data de Abertura da conta: {self.formatar_data_hora(self.data_criacao)} \n")
            arquivo.write("___________________________________\n")

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
        

    @staticmethod
    def conta_existe(numero_conta):
        with open("dados_contas.csv", "r") as arquivo:
            for linha in arquivo:
                if f"| Numero da Conta: {numero_conta} " in linha:
                    return True
        return False

    @staticmethod
    def fazer_saque():
        numero_conta = int(input("Digite o número da conta para saque: "))

        if not Conta.conta_existe(numero_conta):
            print(f"A conta {numero_conta} não existe.")
            return

        valor_saque = float(input("Digite o valor do saque: "))

        # Abrir o arquivo para leitura e escrita
        with open("dados_contas.csv", "r") as arquivo:
            linhas = arquivo.readlines()

        # Percorrer as linhas e encontrar a linha correspondente à conta
        for i, linha in enumerate(linhas):
            if f"| Numero da Conta: {numero_conta} " in linha:
                # Extrair o saldo da linha
                saldo = float(linhas[i + 1].split(": ")[1].strip())
                limite = float(linhas[i + 2].split(": ")[1].strip())

                # Inicializar novo_saldo com o valor atual do saldo
                novo_saldo = saldo

                # Verificar se o saque é válido
                if 0 <= valor_saque <= saldo and valor_saque <= limite:
                    novo_saldo = saldo - valor_saque
                    
                    # Criar uma instância do objeto Historico para salvar a movimentação de saque
                    historico = Historico(numero_conta, datetime.now(), f"Saque de R${valor_saque:.2f}", datetime.now())
                    historico.salvar_arquivo_movimentações()
                # Atualizar o arquivo com o novo saldo
                linhas[i + 1] = f"| Saldo da Conta: {novo_saldo}   \n"

                # Abrir o arquivo para escrita e sobrescrever as linhas
                with open("dados_contas.csv", "w") as arquivo:
                    arquivo.writelines(linhas)

                if 0 <= valor_saque <= saldo and valor_saque <= limite:

                    
                    print(f"Saque de R${valor_saque:.2f} realizado com sucesso na conta {numero_conta}.")
                else:
                    print("Erro: Saque inválido. Verifique o valor do saque e o limite da conta.")
                return

        # Se o loop terminar sem encontrar a conta, exibir mensagem de erro
        print(f"A conta {numero_conta} não foi encontrada no arquivo.")


    @staticmethod
    def fazer_deposito():
        numero_conta = int(input("Digite o número da conta para depósito: "))

        if not Conta.conta_existe(numero_conta):
            print(f"A conta {numero_conta} não existe.")
            return

        valor_deposito = float(input("Digite o valor do depósito: "))

        # Abrir o arquivo para leitura e escrita
        with open("dados_contas.csv", "r") as arquivo:
            linhas = arquivo.readlines()

        # Percorrer as linhas e encontrar a linha correspondente à conta
        for i, linha in enumerate(linhas):
            if f"| Numero da Conta: {numero_conta} " in linha:
                # Calcular o novo saldo
                saldo = float(linhas[i + 1].split(": ")[1].strip())
                novo_saldo = saldo + valor_deposito

                # Criar uma instância do objeto Historico para salvar a movimentação de saque
                historico = Historico(numero_conta, datetime.now(), f"Deposito de R${valor_deposito:.2f}", datetime.now())
                historico.salvar_arquivo_movimentações()

                # Atualizar o arquivo com o novo saldo
                linhas[i + 1] = f"| Saldo da Conta: {novo_saldo}   \n"

                # Abrir o arquivo para escrita e sobrescrever as linhas
                with open("dados_contas.csv", "w") as arquivo:
                    arquivo.writelines(linhas)

                print(f"Depósito de R${valor_deposito:.2f} realizado com sucesso na conta {numero_conta}.")
                return

        # Se o loop terminar sem encontrar a conta, exibir mensagem de erro
        print(f"A conta {numero_conta} não foi encontrada no arquivo.")



    @staticmethod
    def fazer_transferencia():
        # Obter os números das contas envolvidas na transferência
        conta_origem = int(input("Digite o número da conta de origem: "))
        conta_destino = int(input("Digite o número da conta de destino: "))

        # Verificar se ambas as contas existem
        if not Conta.conta_existe(conta_origem) or not Conta.conta_existe(conta_destino):
            print("Uma das contas não existe. Verifique os números das contas.")
            return

        # Obter o valor da transferência
        valor_transferencia = float(input("Digite o valor da transferência: "))

        # Abrir o arquivo para leitura e escrita
        with open("dados_contas.csv", "r") as arquivo:
            linhas = arquivo.readlines()

        # Percorrer as linhas e encontrar as linhas correspondentes às contas de origem e destino
        for i, linha in enumerate(linhas):
            if f"| Numero da Conta: {conta_origem} " in linha:
                # Extrair o saldo da conta de origem
                saldo_origem = float(linhas[i + 1].split(": ")[1].strip())

                # Verificar se há saldo suficiente para a transferência
                if valor_transferencia > saldo_origem:
                    print("Erro: Saldo insuficiente na conta de origem.")
                    return

                # Calcular o novo saldo da conta de origem
                novo_saldo_origem = saldo_origem - valor_transferencia
                # Criar uma instância do objeto Historico para salvar a movimentação de saque
                historico = Historico(conta_origem, datetime.now(), f"Transferencia de R${valor_transferencia:.2f} ", datetime.now())
                historico.salvar_arquivo_movimentações()

                # Atualizar o arquivo com o novo saldo da conta de origem
                linhas[i + 1] = f"| Saldo da Conta: {novo_saldo_origem}   \n"

            elif f"| Numero da Conta: {conta_destino} " in linha:
                # Extrair o saldo da conta de destino
                saldo_destino = float(linhas[i + 1].split(": ")[1].strip())

                # Calcular o novo saldo da conta de destino
                novo_saldo_destino = saldo_destino + valor_transferencia

                # Atualizar o arquivo com o novo saldo da conta de destino
                linhas[i + 1] = f"| Saldo da Conta: {novo_saldo_destino}   \n"

        # Abrir o arquivo para escrita e sobrescrever as linhas
        with open("dados_contas.csv", "w") as arquivo:
            arquivo.writelines(linhas)

        print(f"Transferência de R${valor_transferencia:.2f} realizada com sucesso da conta {conta_origem} para a conta {conta_destino}.")

    
    @classmethod
    def imprimir_contas(cls):
        with open("dados_contas.csv", "r") as arquivo:
            linhas = arquivo.readlines()
            for linha in linhas:
                print(linha)    