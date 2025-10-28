from funcion import*
from classes import*


clientes = {}
while True:
    try:
        match menu_login():
            case 1:#cadastro de cliente
                LP()
                try:
                    nome = input("Nome completo: ")
                    cpf = int(input("CPF (somente números): "))
                    telefone = int(input("Telefone (somente números): "))
                    endereco = input("Endereço: ")
                    nascimento = input("Data de nascimento (DD/MM/AAAA): ")
                    senha = input("Senha: ")
                    banco.cadastrar_cliente(nome, cpf, telefone, senha, endereco, nascimento)

                except ValueError:
                    print("Erro no cadastro.CPF e telefone devem conter apenas números.")
                    continue
                LP()
            case 2:  # Cadastro de conta
                LP()
                try:
                    cpf = int(input("CPF do cliente: "))
                except ValueError:
                    print("CPF deve conter apenas números.")
                    continue
                cliente = banco.clientes.get(cpf)
                if not cliente:
                    print("Cliente não encontrado.")
                    continue
                cadastro_conta(cliente)
                LP()

            case 3:  # Login
                LP()
                try:
                    conta = login_conta()
                except ValueError:
                    print("Número da conta deve conter apenas números.")
                    continue
                
                if not conta:
                    continue
                LP()
                while True:
                    LP()
                    try:
                        match menu_principal():
                            case 1:
                                LP()
                                cadastro_conta(conta.get_cliente())
                                LP()
                            case 2:
                                LP()
                                for c in conta.get_cliente().get_contas():
                                    print(f"Conta {c.get_numero()} | Saldo: R${c.get_saldo():.2f}")
                                LP()
                            case 3:
                                LP()
                                depositar(conta)
                                LP()
                            case 4:
                                LP()
                                sacar(conta)
                                LP()
                            case 5:
                                LP()
                                transferir(conta)
                                LP()
                            case 6:
                                LP()
                                consultar_saldo(conta)
                                LP()
                            case 7:
                                LP()
                                conta.mostrar_extrato()
                                LP()
                            case 0:
                                LP()
                                print("Saindo...")
                                LP()
                                break
                            case _:
                                LP()
                                print("Opção inválida!")
                                LP()
                    except ValueError:
                        print("Entrada inválida. digite apenas números válidos para escolher uma opção.")
                        LP()

            case 0:
                print("Obrigada por usar nosso banco!")
                LP()
                break

            case _:
                print("Opção inválida!")
                LP()

    except ValueError:
        print("Entrada inválida. Tente novamente.")