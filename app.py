from funcion import*


resp= input("") # variavel simbolica, é para o macth n dar erro


match menu_login():
    case 1:
        menu_cadastro()
        cadastrar_cliente()
        
    case 2:
        
        match  menu_principal():
            case 1:
                pass
            case 2:
                pass
            case 3:
                pass
            case 4:
                pass
            case 5:
                pass
            case 6:
                pass
            case 7:
                pass
            case 8:
                pass
            case _:
                pass
        
    case 3:
         match  resp:
            case 1:
                pass
            case 2:
                pass
            case 3:
                pass
            case 4:
                pass
            case 5:
                pass
            case 6:
                pass
            case 7:
                pass
            case 8:
                pass
            case _:
                pass
        
    case _ :
        pass