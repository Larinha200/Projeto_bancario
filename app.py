from funcion import*
from classes import*


clientes = {}
while True:
    match menu_login():
        case 1:#cadastro de cliente
            menu_cadastro(clientes)
        case 2:#cadastro de conta
            cadastro_conta(clientes)  
            
        case 3:
            login_cliente(clientes)
            while True:
                match menu_conta():
                    #Login na conta corrente 
                    case 1:  
                        while True:
                            match  menu_principal():
                                case 1:#cadastrar outra conta
                                    menu_contas()
                                    pass

                                case 2:#contas
                                    pass

                                case 3:#depósito
                                    depositar(Conta)

                                case 4:#saque
                                    sacar(Conta)

                                case 5:#tranfarencia entre contas
                                    transferir(Conta)

                                case 6:#Consultar saldo
                                    consultar_saldo(Conta)

                                case 7:#Consultar extrato
                                    mostrar_extrato(Conta)

                                
                                case 0:
                                    break
                                    continue

                                case _:
                                    print("Opção invalida!")
                                
                        
                    #login na conta poupança
                    case 2:
                        match menu_principal():
                            case 1:#cadastrar outra conta
                                menu_contas()
                                pass
                            
                            case 2:#contas
                                pass

                            case 3:#depósito
                                depositar(Conta)

                            case 4:#saque
                                sacar(Conta)

                            case 5:#tranfarencia entre contas
                                transferir(Conta)

                            case 6:#Consultar saldo
                                consultar_saldo(Conta)

                            case 7:#Consultar extrato
                                mostrar_extrato(Conta)

                        
                            case 0:
                                break
                                continue
                            
                            case _:
                                print("Opção invalida!")

                    case 0:
                        break
                    
                    case _:
                        print("Opção invalida!")
   
        case 0:
            print("Obrigada por utilizar nosso banco! ")
            break
        
        case _:
            print("Opção invalida!")