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

Link: https://miro.com/welcomeonboard/T2xuS1lIOGRRUGpubDhwMDJVdWlieGR1UXFPV1pjd1BqZiswZW5aYXBKdHpPU2ttSWs0SVRMRTFpRFYzRzNRS3lvL28rMVdBYTdCdVZuSklVcnl6MkpadzY5TUpBYnFPbmFFeXp3M2x4OTZRUWdFUEpMK09MRmJUU1JSQ3RoNGthWWluRVAxeXRuUUgwWDl3Mk1qRGVRPT0hdjE=?share_link_id=39372193831

![Image](https://github.com/user-attachments/assets/ba2b7ec5-1107-4e15-813a-ff9b4e3f859c)


### Explicação do código em partes → ✩ classes.py

    from abc import ABC, abstractmethod

    class Banco:
        def __init__(self):
            self.clientes = {}  # {cpf: cliente}

    def cadastrar_cliente(self, nome, cpf, telefone, senha, endereco, nascimento):
        if cpf in self.clientes:
            print(f"\nJá existe um cliente com o CPF {cpf} cadastrado!")
            return self.clientes[cpf]

        novo_cliente = Cliente(nome, cpf, telefone, senha, endereco, nascimento)
        self.clientes[cpf] = novo_cliente
        print(f"\nCliente {nome} cadastrado com sucesso!")
        return novo_cliente

    class Cliente:
        count = 0
        def __init__(self, nome, cpf, telefone, senha, endereco, nascimento):
            Cliente.count += 1
            self.__id = Cliente.count
            self.__nome = nome
            self.__cpf = cpf
            self.__telefone = telefone
            self.__senha = senha
            self.__endereco = endereco
            self.__nascimento = nascimento
            self.__contas = []

    def get_id(self): return self.__id
    def get_nome(self): return self.__nome
    def get_cpf(self): return self.__cpf
    def get_telefone(self): return self.__telefone
    def get_senha(self): return self.__senha
    def get_endereco(self): return self.__endereco
    def get_nascimento(self): return self.__nascimento
    def get_contas(self): return self.__contas

    def add_conta(self, conta):
        self.__contas.append(conta)

    class OperacoesFinanceiras(ABC):
        @abstractmethod
        def depositar(self, valor): pass
        @abstractmethod
        def sacar(self, valor): pass
        @abstractmethod
        def transferir(self, destino, valor): pass
    
    class Extrato:
        def __init__(self):
            self.__transacoes = []

    def registrar(self, tipo, valor, saldo):
        self.__transacoes.append({"tipo": tipo, "valor": valor, "saldo": saldo})

    def mostrar(self):
        print("Extrato:")
        for t in self.__transacoes:
            print(f"{t['tipo']}: R${t['valor']:.2f} | Saldo: R${t['saldo']:.2f}")

    class Conta(OperacoesFinanceiras):
        def __init__(self, numero, cliente, senha):
            self.__numero = numero
            self.__cliente = cliente
            self.__senha = senha
            self.__saldo = 0.0
            self.__extrato = Extrato()

    def get_numero(self): return self.__numero
    def get_cliente(self): return self.__cliente
    def get_saldo(self): return self.__saldo
    def get_senha(self): return self.__senha

    def depositar(self, valor):
        if valor <= 0:
            print("Erro: valor deve ser positivo")
            return False
        self.__saldo += valor
        self.__extrato.registrar("Depósito", valor, self.__saldo)
        print(f"Depósito de R${valor:.2f} realizado.")
        return True

    def transferir(self, destino, valor):
        if self.sacar(valor):
            destino.depositar(valor)
            self.__extrato.registrar(f"Transferência p/ conta {destino.get_numero()}", valor, self.__saldo)
            print(f"Transferência de R${valor:.2f} realizada.")
            return True
        return False

    def mostrar_extrato(self):
        print(f"\nExtrato da conta {self.__numero}:")
        self.__extrato.mostrar()

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

    from classes import Banco, ContaCorrente, ContaPoupanca
    
    banco = Banco()
    
    def menu_login():
        print("\n1- Cadastro de cliente\n2- Cadastro de conta\n3- Login\n0- Sair")
        return int(input("---> "))
    
    def menu_conta():
        print("\n1- Login Conta Corrente\n2- Login Conta Poupança\n0- Sair")
        return int(input("---> "))
    
    def menu_principal():
        print("\n1- Cadastrar outra conta\n2- Listar contas\n3- Depósito\n4- Saque\n5- Transferência\n6- Consultar saldo\n7- Extrato\n0- Sair")
        return int(input("---> "))
    
    # Funções auxiliares
    def cadastro_conta(cliente):
        tipo = int(input("Tipo de conta (1-Poupança, 2-Corrente): "))
        senha = input("Senha da conta: ")
        numero = len(cliente.get_contas()) + 1

    if tipo == 1:
        conta = ContaPoupanca(numero, cliente, senha)
        print(f"Conta Poupança criada! Número: {numero}")
    elif tipo == 2:
        conta = ContaCorrente(numero, cliente, senha)
        print(f"Conta Corrente criada! Número: {numero}")
    else:
        print("Tipo inválido.")
        return None

    cliente.add_conta(conta)
    return conta

    def login_conta():
        numero = int(input("Número da conta: "))
        senha = input("Senha: ")
        for cliente in banco.clientes.values():
            for conta in cliente.get_contas():
                if conta.get_numero() == numero and conta.get_senha() == senha:
                    print(f"Login bem-sucedido! {cliente.get_nome()}")
                    return conta
        print("Conta ou senha inválidos.")
        return None
    
    def depositar(conta):
        valor = float(input("Valor do depósito: "))
        conta.depositar(valor)
    
    def sacar(conta):
        valor = float(input("Valor do saque: "))
        conta.sacar(valor)
    
    def transferir(conta):
        destino_num = int(input("Número da conta destino: "))
        valor = float(input("Valor da transferência: "))
        for cliente in banco.clientes.values():
            for c in cliente.get_contas():
                if c.get_numero() == destino_num:
                    conta.transferir(c, valor)
                    return
        print("Conta destino não encontrada.")
    
    def consultar_saldo(conta):
        print(f"Saldo: R${conta.get_saldo():.2f}")
   
![Image](https://github.com/user-attachments/assets/ba2b7ec5-1107-4e15-813a-ff9b4e3f859c)


### Explicação do código em partes → ✩ app.py

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

   
            break
        
        case _:
            print("Opção invalida!")  #Exibe mensagem se o usuário digitar algo fora das opções do menu principal.
