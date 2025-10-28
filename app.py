from funcion import*
from classes import*


clientes = {}
while True:
    try:
        match menu_login():
            case 1:#cadastro de cliente
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
            case 2:  # Cadastro de conta
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

            case 3:  # Login
                try:
                    conta = login_conta()
                except ValueError:
                    print("Número da conta deve conter apenas números.")
                    continue
                
                if not conta:
                    continue
                
                while True:
                    try:
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
                    except ValueError:
                        print("Entrada inválida. digite apenas números válidos para escolher uma opção.")

            case 0:
                print("Obrigada por usar nosso banco!")
                break

            case _:
                print("Opção inválida!")
    except ValueError:
        print("Entrada inválida. Tente novamente.")