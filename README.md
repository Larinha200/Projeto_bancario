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

    from abc import ABC, abstractmethod #importar a biblioteca ABC
    
    #criação das classes 
    class Banco:
        def __init__(self):
            self.__clientes = {}# Dicionário para guardar os clientes do banco
    
    
        def cadastrar_cliente(self,nome, cpf, telefone, senha, endereco, nascimento, clientes):
            # Se CPF já cadastrado, mostra aviso e retorna o cliente existente
            if cpf in clientes:
                print(f"\n Já existe um cliente com o CPF {cpf} cadastrado!")
                return clientes[cpf]
    
            # Cria e adiciona novo cliente ao dicionario
            novo_cliente = Cliente(nome, cpf, telefone, senha, endereco, nascimento)
            self.__clientes[cpf] = novo_cliente
            return novo_cliente


        class Cliente:
            count = 0 # contador para dar um "id" diferente pra cada cliente
    
        def __init__(self, nome: str, cpf:int, telefone:int, senha: str, endereco:str,nascimento:int ):
            Cliente.count += 1 # aumenta o contador
            self.__id = Cliente.count # cria um id único pra cada cliente
            self.__nome = nome
            self.__cpf = cpf
            self.__telefone = telefone
            self.__endereco = endereco
            self.__nascimento = nascimento
            self.__senha = senha
            self.__conta = [] # lista que vai guardar as contas do cliente
        

        #GETS para acessar atributos privados da classe cliente
            def getId(self):
                return self.__id
            
        def getNome(self):
            return self.__nome
        
        def getCpf(self):
            return self.__cpf
        
        def getConta(self):
            return self.__conta
        
        def getTelefone(self):
            return self.__telefone
        
        def getSenha(self):
            return self.__senha 
        
        def getEndereco(self):
            return self.__endereco
        
        def getNascimento(self):
            return self.__nascimento
        
        
        #Def para adicionar conta ao cliente
        def add_conta(self, conta):
            return self.__conta.append(conta)
        
    
    
            
            # Interface para operações financeiras
            class OperacoesFinanceiras(ABC):
                #metodo abstrato para depositar
                @abstractmethod
                def depositar(self, valor: float):
                    pass
        
            #metodo abstrato para sacar
            @abstractmethod
            def sacar(self, valor: float):
                pass
            
            #metodo abstrato para transferir
            @abstractmethod
            def transferir(self, destino, valor: float):
                pass
            
            
            class Extrato:
                def __init__(self):
                    self.__transacoes = [] # lista de dicionários com as transações
        
            # Adiciona um dicionário com os detalhes da transacao à lista de transacoes
            def registrar(self, tipo: str, valor: float, saldo: float):
                self.__transacoes.append({'tipo': tipo, 'valor': valor,'saldo': saldo })
        
            #Exibe todas as transações registradas no extrato
            def mostrar(self):
                # .2f significa que pode ter dois caracteres depois da virgula
                for transacao in self.__transacoes:
                    return (f"{transacao['tipo']}: R${transacao['valor']:.2f} | Saldo: R${transacao['saldo']:.2f}")


        class Conta(OperacoesFinanceiras):
            def __init__(self, numero: int, cliente: Cliente, senha: str):
                self.__numero = numero
                self.__cliente = cliente
                self.__senha = senha  # senha da conta
                self.__saldo = 0.0
                self.__extrato = Extrato()
                
        
        #GETS para acessar atributos privados da classe conta
        def getNumero(self):
            return self.__numero
    
        def getCliente(self):
            return self.__cliente
        
        def getSaldo(self):
            return self.__saldo
        
        def getSenha(self):
            return self.__senha
    
    # Método para depositar
        def depositar(self, valor: float):
            if valor <= 0:
                print(" Valor invalido o depósito deve ser positivo.")
            else:
                self.__saldo += valor
                self.__extrato.registrar("Depósito", valor, self.__saldo)
                print(f"Depósito de R${valor:.2f} realizado com sucesso.")
            
    
    #mostrar extrato da conta
        def mostrar_extrato(self):
            print(f"Extrato da conta {self.__numero}:")
            self.__extrato.mostrar()


    #transferir saldo para uma conta
        def transferir(self, destino, valor: float):
            if self.__sacar(valor):
                destino.depositar(valor)
                self.__extrato.registrar(f"Transferência para conta {destino.getNumero()}", valor, self.__saldo)
                print(f"Transferência de R${valor:.2f} concluída.")
                return True
            return False

    # método para consultar o saldo da conta
        def consultar_saldo(self):
            return (f"Saldo da conta {self.__numero}: R${self.__saldo:.2f}")


        class ContaCorrente(Conta):
            def __init__(self, numero, cliente, senha):
                self.__senha = senha
                super().__init__(numero, cliente, senha)

    #get para senha
        def getSenha(self):
            return self.__senha
    
    #sacar valor na conta
        def sacar(self, valor: float):
            if valor <= self.__saldo and valor > 0:
                self.__Conta_saldo -= valor
                self.__Conta_extrato.registra ("Saque", valor, self.__saldo)
                return True
            else:
                ("Saldo insuficiente ou valor inválido para saque.")
                return False

        class ContaCorrente(Conta):
            def sacar(self, valor):
                if valor > 0 and valor <= self.get_saldo():
                    self._Conta__saldo -= valor
                    self._Conta__extrato.registrar("Saque", valor, self.get_saldo())
                    print(f"Saque de R${valor:.2f} realizado.")
                    return True
                print("Saldo insuficiente ou valor inválido.")
                return False
        
        class ContaPoupanca(Conta):
            SALDO_MINIMO = 100.0
            def sacar(self, valor):
                if valor > 0 and (self.get_saldo() - valor) >= self.SALDO_MINIMO:
                    self._Conta__saldo -= valor
                    self._Conta__extrato.registrar("Saque", valor, self.get_saldo())
                    print(f"Saque de R${valor:.2f} realizado.")
                    return True
                print(f"Não é permitido sacar. Saldo mínimo R${self.SALDO_MINIMO:.2f}")
                return False

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
