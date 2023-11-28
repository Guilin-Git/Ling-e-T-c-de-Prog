import pandas
from datetime import datetime
from Cliente import Cliente

class Historico:
    def __init__(self, numero_conta, dt_abertura, movimento, dt_movimento):
        self.numero_conta = numero_conta
        self.dt_abertura = dt_abertura
        self.movimento = movimento
        self.dt_movimento = dt_movimento

    def salvar_arquivo(self):
        with open("Historico_Contas.csv", "a") as arquivo:
            arquivo.write("_______________________________________________\n")
            arquivo.write(f"| Numero da Conta: {self.numero_conta} \n")
            arquivo.write(f"| Data de Abertura da conta: {self.formatar_data_hora(self.dt_abertura)} \n")
            arquivo.write(f"| Tipo de movimentação: {self.movimento}   \n")
            arquivo.write(f"| Data da movimentação: {self.formatar_data_hora(self.dt_movimento)}   \n")
            arquivo.write("_______________________________________________\n")

    def salvar_arquivo_movimentações(self):
        with open("Historico_Contas.csv", "a") as arquivo:
            arquivo.write("_______________________________________________\n")
            arquivo.write(f"| Numero da Conta: {self.numero_conta} \n")
            arquivo.write(f"| Tipo de movimentação: {self.movimento}   \n")
            arquivo.write(f"| Data da movimentação: {self.formatar_data_hora(self.dt_movimento)}   \n")
            arquivo.write("_______________________________________________\n")        

    @staticmethod
    def formatar_data_hora(data_hora):
        return data_hora.strftime("%d/%m/%Y %H:%M:%S")
    
    def adicionar_movimentacao(self, movimentacao):
        self.movimentos.append(movimentacao)
    
    
    @classmethod
    def imprimir_historico(cls):
        numero_conta = int(input("Digite o número da conta para imprimir o histórico: "))
        conta_existe = cls.verificar_conta_existente(numero_conta)
        if not conta_existe:
            print(f"A conta {numero_conta} ainda não foi criada.")
            return

        with open("Historico_Contas.csv", "r") as arquivo:
            historico_encontrado = False
            for linha in arquivo:
                if f"| Numero da Conta: {numero_conta} " in linha:
                    historico_encontrado = True
                elif historico_encontrado:
                    if "_______________________________________________" in linha:
                        break
                    print(linha.strip())

    @staticmethod
    def verificar_conta_existente(numero_conta):
        with open("dados_contas.csv", "r") as arquivo:
            for linha in arquivo:
                if f"| Numero da Conta: {numero_conta} " in linha:
                    return True
        return False

    @classmethod
    def imprimir_movimentacoes_conta(cls, numero_conta):
        conta_existe = cls.verificar_conta_existente(numero_conta)
        if not conta_existe:
            print(f"A conta {numero_conta} ainda não foi criada.")
            return

        with open("Historico_Contas.csv", "r") as arquivo:
            historico_encontrado = False

            for linha in arquivo:
                if f"| Numero da Conta: {numero_conta} " in linha:
                    historico_encontrado = True
                elif historico_encontrado and "_______________________________________________" in linha:
                    historico_encontrado = False
                elif historico_encontrado:
                    # Separar a linha em chave e valor
                    chave, valor = map(str.strip, linha.strip().split(":", 1))
                    # Imprimir a chave e valor, adicionando '\n' após o horário
                    print(f"{chave}: {valor}", end='\n' if "Data da movimentação" in linha else '')









