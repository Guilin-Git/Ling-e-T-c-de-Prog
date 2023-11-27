from Cliente import Cliente
from Conta import Conta

def main():
    while True:
        print("\nEscolha uma opção:")
        print("1 - Cadastrar Cliente")
        print("2 - Imprimir Clientes")
        print("3 - Cadastrar Conta")
        print("4 - Fazer Saque")
        print("5 - Fazer Depósito")
        print("6 - Imprimir Contas")
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
            Conta.imprimir_contas()
        elif opcao == "0":
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()