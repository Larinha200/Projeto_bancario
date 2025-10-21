from funcion import*
from classes import*


clientes = {}
while True:
    match menu_login():
        
        case 1:
            menu_cadastro(clientes)
  
        case 2:
            
            match  menu_principal():
                case 1:
                    pass
                case 2:
                    pass
                case 3:
                    depositar(Conta)
                case 4:
                    sacar(Conta)
                case 5:
                    transferir(Conta)
                case 6:
                    consultar_saldo(Conta)
                case 7:
                    mostrar_extrato(Conta)
                case 8:
                    pass
                case _:
                    pass
            
        case 3:
            match menu_principal():
                case 1:
                    pass
                case 2:
                    pass
                case 3:
                    depositar(Conta)
                case 4:
                    sacar(Conta)
                case 5:
                    transferir(Conta)
                case 6:
                    consultar_saldo(Conta)
                case 7:
                    mostrar_extrato(Conta)
                case 8:
                    pass
                case _:
                    pass
        case 4:
            listar_clientes(clientes)
    
        case _ :
            pass