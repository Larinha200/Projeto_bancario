from funcion import*
from classes import*


clientes = {}
while True:
    match menu_login():
        case 1:#cadastro de cliente
            nome = input("Nome completo: ")
            cpf = int(input("CPF (somente números): "))
            telefone = int(input("Telefone (somente números): "))
            endereco = input("Endereço: ")
            nascimento = input("Data de nascimento (DD/MM/AAAA): ")
            senha = input("Senha: ")
            banco.cadastrar_cliente(nome, cpf, telefone, senha, endereco, nascimento)
        
        case 2:  # Cadastro de conta
            cpf = int(input("CPF do cliente: "))
            cliente = banco.clientes.get(cpf)
            if not cliente:
                print("Cliente não encontrado.")
                continue
            cadastro_conta(cliente)

        case 3:  # Login
            conta = login_conta()
            if not conta:
                continue
            while True:
                match menu_principal():
                    case 1:
                        cadastro_conta(conta.get_cliente())
                    case 2:
                        for c in conta.get_cliente().get_contas():
                            print(f"Conta {c.get_numero()} | Saldo: R${c.get_saldo():.2f}")
                    case 3:
                        depositar(conta)
                    case 4:
                        sacar(conta)
                    case 5:
                        transferir(conta)
                    case 6:
                        consultar_saldo(conta)
                    case 7:
                        conta.mostrar_extrato()
                    case 0:
                        break
                    case _:
                        print("Opção inválida!")

        case 0:
            print("Obrigada por usar nosso banco!")
            break

        case _:
            print("Opção inválida!")