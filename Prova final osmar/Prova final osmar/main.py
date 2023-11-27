from Cliente import Cliente
from Conta import Conta
from Historico import Historico

def main():
    while True:
        print("\nEscolha uma opção:")
        print("1 - Cadastrar Cliente")
        print("2 - Imprimir Clientes")
        print("3 - Cadastrar Conta")
        print("4 - Fazer Saque")
        print("5 - Fazer Depósito")
        print("6 - Fazer Transferencia")
        print("7 - Imprimir Contas")
        print("8 - Data de Abertura da conta")
        print("9 - Imprimir Movimentações de Conta")
        print("0 - Sair")

        opcao = input("Digite o número da opção desejada: ")

        if opcao == "1":
            Cliente.Cadastro_Cliente()
        elif opcao == "2":
            Cliente.Imprimir_cadastro()
        elif opcao == "3":
            Conta.Cadastro_Conta()
        elif opcao == "4":
            Conta.fazer_saque()
        elif opcao == "5":
            Conta.fazer_deposito()
        elif opcao == "6":
            Conta.fazer_transferencia()
        elif opcao == "7":
            Conta.imprimir_contas()
        elif opcao == "8":
            Historico.imprimir_historico()
        elif opcao == "9":
            numero_conta = int(input("Digite o número da conta para imprimir as movimentações: "))
            Historico.imprimir_movimentacoes_conta(numero_conta)
        elif opcao == "0":
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()