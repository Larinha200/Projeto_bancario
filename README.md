# Projeto Bancário

![Image](https://github.com/user-attachments/assets/ba2b7ec5-1107-4e15-813a-ff9b4e3f859c)

***Objetivo inicial do projeto →***

O cenário na qual nos foi designado como equipe visa com que desenvolvamos um sistema de gestão de contas bancárias, permitindo questões básicas e necessárias para a utilização do sistema (Cadastro de clientes, criação de conta, depósitos, saques, transferênicas e consulta de saldos.) Além de também habilitar a utilização e seleção de diferentes tipos de conta (Poupança e Corrente), possibilitando com que o sistema abranja diversos tipos de clientes e possibilidades, fazendo com que o projeto seja o mais elaborado possível para sua execução. 

![Image](https://github.com/user-attachments/assets/ba2b7ec5-1107-4e15-813a-ff9b4e3f859c)

### Requisitos técnicos  →

→ ***Classes e Objetos:*** São conceitos fundamentais da programação orientada a objetos, onde a classe é o "molde" ou "planta" que define as características (atributos) e comportamentos (métodos) de um tipo de coisa, enquanto o objeto é uma "instância" concreta dessa classe.  
<br><br> → ***Encapsulamento:*** É um conceito de programação orientada a objetos que agrupa dados (atributos) e os métodos que operam sobre eles em uma única unidade (classe).
<br><br> → ***Herança:*** Herança é um pilar da programação orientada a objetos (POO) que permite que uma classe (filha) reutilize atributos e métodos de outra classe (pai).
<br><br> → ***Polimorfismo:*** É a capacidade de objetos de diferentes classes serem tratados de maneira uniforme, usando uma interface ou método comum. 
<br><br> → ***Abstração:*** Classes abstratas servem como um molde (blueprint) para outras classes.
<br><br> → ***Associação:*** Os objetos estão conectados, mas existem de forma independente. Um objeto pode interagir com o outro, mas sua existência não depende dele.
<br><br> → ***Agregação:***  Um objeto "todo" é composto por outros objetos "parte", mas as partes podem existir independentemente do todo.
<br><br> → ***Composição:***  O objeto "parte" não pode existir sem o objeto "todo".
<br><br> → ***Sobrecarga de métodos:*** Sobrecarga de método significa ter vários métodos com o mesmo nome numa classe, mas com assinaturas diferentes (parâmetros diferentes).
<br><br> → ***Interfaces:*** Uma interface de programação (abstrata), que define um contrato de métodos que outras classes devem implementar, ou uma interface gráfica (GUI), que é a parte visual de um programa.

### Porque foram utilizados (resumo) →

✩ ***Classes e Objetos:***
<br><br> ✩ ***Encapsulamento:***
<br><br> ✩ ***Herança:***
<br><br> ✩ ***Polimorfismo:***
<br><br> ✩ ***Abstração:***
<br><br> ✩ ***Associação:***
<br><br> ✩ ***Agregação:***
<br><br> ✩ ***Composição:***
<br><br> ✩ ***Sobrecarga de métodos:***
<br><br> ✩ ***Interfaces:*** 

![Image](https://github.com/user-attachments/assets/ba2b7ec5-1107-4e15-813a-ff9b4e3f859c)

## Requisitos funcionais →

✩ ***O sistema deve gerenciar clientes e suas contas bancárias.***
<br><br>✩ ***Depósito***
<br><br>✩ ***Saque***
<br><br>✩ ***Transferência entre contas***
<br><br>✩ ***Consulta de saldo e extrato***
<br><br>✩ ***Conta Corrente: permite saques sem saldo mínimo.***
<br><br>✩ ***Conta Poupança: exige saldo mínimo de R$ 100,00 para saques.***
<br><br>✩ ***Um cliente pode possuir mais de uma conta no banco.***
<br><br>✩ ***Todas as operações devem ser registradas em um extrato vinculado à conta.***

![Image](https://github.com/user-attachments/assets/ba2b7ec5-1107-4e15-813a-ff9b4e3f859c)

### Diagrama de Classes UML →

*diagraminha aqui com talvez uma breve explicaçãozinha????*

![Image](https://github.com/user-attachments/assets/ba2b7ec5-1107-4e15-813a-ff9b4e3f859c)


### Explicação do código em partes → ✩ classes.py



![Image](https://github.com/user-attachments/assets/ba2b7ec5-1107-4e15-813a-ff9b4e3f859c)


### Explicação do código por partes → ✩ funcion.py



![Image](https://github.com/user-attachments/assets/ba2b7ec5-1107-4e15-813a-ff9b4e3f859c)


### Explicação do código em partes → ✩ app.py



    from funcion import*  #Está importando todas as funções do arquivo funcion.py
    from classes import*  #Está importando todas as classes do arquivos classes.py


      clientes = {}  #Cria um dicion[ario onde guardara informações sobre os clientes e suas contas
      while True:  #Inicia um looping infinito (só ira encerrar quando tiver um break)
          match menu_login(): #Chama a função menu_login() -> O match testa o valor de uma expressão e executa o bloco correspondente ao padrão que combina com esse valor
          
            case 1:#cadastro de cliente 
                menu_cadastro(clientes) 
                
                  case 2:#cadastro de conta
                  cadastro_conta(clientes)  
            
        case 3: #login de clientes
            login_cliente(clientes)
            
            while True: #Abre outro looping
                match menu_conta(): #Chama menu_conta() 
                        
                    case 1:  #Se o usuário escolher 1, ele entra no sistema da conta corrente.
                        login_conta(clientes) 
                        
                        while True: #Outro loop começa.
                            match  menu_principal():
                            
                                case 1:#cadastrar outra conta
                                    menu_contas()   #
                                    pass   #Evita erro de bloco vazio 

                                case 2:#contas
                                    pass   #Evita erro de bloco vazio 

                                case 3:#depósito
                                    depositar(cliente)  #Chama a função depositar() 

                                case 4:#saque
                                    Conta.sacar(Conta)  

                                case 5:#tranfarencia entre contas
                                    Conta.transferir(Conta, destino, valor)

                                case 6:#Consultar saldo
                                    Conta.consultar_saldo(Conta)  #Exibe o saldo atual da conta.

                                case 7:#Consultar extrato
                                    Conta.mostrar_extrato()   #Exibe todas as movimentações da conta.

                                
                                case 0:    
                                    break    #Sai do loop atual (menu principal)
                                    continue   #Pula para o início do próximo loop

                                case _:
                                    print("Opção invalida!")  #Executado se o usuário digitar uma opção inexistente.
                                
                        
                    #login na conta poupança
                    case 2:
                        match menu_principal():
                            case 1:#cadastrar outra conta
                                menu_contas()
                                pass   #Evita erro de bloco vazio 
                            
                            case 2:#contas
                                pass   #Evita erro de bloco vazio 

                            case 3:#depósito
                                depositar(cliente)

                            case 4:#saque
                                Conta.sacar()

                            case 5:#tranfarencia entre contas
                                Conta.transferir(Conta, destino, valor)

                            case 6:#Consultar saldo
                                Conta.consultar_saldo()

                            case 7:#Consultar extrato
                                Conta.mostrar_extrato()

                        
                            case 0:
                                break  #Sai do segundo while True (menu_conta), voltando para o menu de login.
                          
                            
                            case _:
                                print("Opção invalida!")  #Exibe mensagem se o usuário digitar uma opção que não existe.

                    case 0:
                        break
                    
                    case _:
                        print("Opção invalida!")  #Exibe mensagem se o usuário digitar uma opção que não existe.
   
        case 0:
            print("Obrigada por utilizar nosso banco! ")  #Sai do primeiro while True e encerra o programa.
            break
        
        case _:
            print("Opção invalida!")  #Exibe mensagem se o usuário digitar algo fora das opções do menu principal.
