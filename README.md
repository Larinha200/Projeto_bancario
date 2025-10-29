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

![Image](https://github.com/user-attachments/assets/ba2b7ec5-1107-4e15-813a-ff9b4e3f859c)

### Porque foram utilizados (resumo) →

✩ ***Classes e Objetos:*** Usados para representar de forma organizada os elementos do banco, como clientes e contas, deixando o código mais realista e fácil de entender.
<br><br> ✩ ***Encapsulamento*** Protege dados importantes (como saldo e senha) e impede alterações diretas, garantindo segurança e controle das operações. 
<br><br> ✩ ***Herança:*** Evita repetição de código, permitindo criar tipos de contas diferentes (corrente, poupança) que compartilham as mesmas funções básicas.
<br><br> ✩ ***Polimorfismo:*** Permite usar os mesmos métodos com comportamentos diferentes, como sacar() funcionando de forma distinta em cada tipo de conta.
<br><br> ✩ ***Abstração:*** Simplifica o uso do sistema, escondendo a lógica interna e mostrando apenas o que o usuário precisa (como depositar ou sacar).
<br><br> ✩ ***Associação:*** Conecta classes que trabalham juntas, como o cliente que possui contas, sem que uma dependa totalmente da outra.
<br><br> ✩ ***Agregação:*** Representa quando uma classe contém outras, como um cliente com várias contas, mas cada uma ainda existe separadamente.
<br><br> ✩ ***Composição:*** Usada quando um objeto depende totalmente do outro, como o extrato que só existe dentro da conta.
<br><br> ✩ ***Sobrecarga de métodos:*** Permite usar o mesmo método de formas diferentes, tornando o sistema mais flexível e adaptável.
<br><br> ✩ ***Interfaces:*** Garantem que todas as classes sigam o mesmo padrão de funções obrigatórias, mantendo o sistema organizado e coerente.

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

(Duas opções de diagrama)

Link no Canva: https://www.canva.com/design/DAG3GQ50JkE/KgJLXkbRUEPcBgUKXVf5VQ/edit?utm_content=DAG3GQ50JkE&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton

Link no Miro: https://miro.com/welcomeonboard/T2xuS1lIOGRRUGpubDhwMDJVdWlieGR1UXFPV1pjd1BqZiswZW5aYXBKdHpPU2ttSWs0SVRMRTFpRFYzRzNRS3lvL28rMVdBYTdCdVZuSklVcnl6MkpadzY5TUpBYnFPbmFFeXp3M2x4OTZRUWdFUEpMK09MRmJUU1JSQ3RoNGthWWluRVAxeXRuUUgwWDl3Mk1qRGVRPT0hdjE=?share_link_id=39372193831

![Image](https://github.com/user-attachments/assets/ba2b7ec5-1107-4e15-813a-ff9b4e3f859c)


### Explicação do código em partes → ✩ classes.py

    # Importa classes abstratas e métodos abstratos
    from abc import ABC, abstractmethod
    
    
    # ------------------- CLASSE BANCO -------------------
   
    class Banco:
        def __init__(self):
            # Dicionário para armazenar os clientes cadastrados
            # A chave é o CPF e o valor é o objeto Cliente
            self.clientes = {}  

    def cadastrar_cliente(self, nome, cpf, telefone, senha, endereco, nascimento):
        # Verifica se o cliente já está cadastrado
        if cpf in self.clientes:
            print(f"\nJá existe um cliente com o CPF {cpf} cadastrado!")
            return self.clientes[cpf]

        # Cria um novo cliente e o adiciona ao dicionário de clientes
        novo_cliente = Cliente(nome, cpf, telefone, senha, endereco, nascimento)
        self.clientes[cpf] = novo_cliente
        print(f"\nCliente {nome} cadastrado com sucesso!")
        return novo_cliente

    
    # ------------------- CLASSE CLIENTE -------------------
    
    class Cliente:
        count = 0  # Contador estático para gerar IDs únicos

    def __init__(self, nome, cpf, telefone, senha, endereco, nascimento):
        Cliente.count += 1  # Incrementa o ID a cada novo cliente criado
        self.__id = Cliente.count
        self.__nome = nome
        self.__cpf = cpf
        self.__telefone = telefone
        self.__senha = senha
        self.__endereco = endereco
        self.__nascimento = nascimento
        self.__contas = []  # Lista para armazenar as contas do cliente

    # Métodos getters — usados para acessar os atributos privados com segurança
    def get_id(self): return self.__id
    def get_nome(self): return self.__nome
    def get_cpf(self): return self.__cpf
    def get_telefone(self): return self.__telefone
    def get_senha(self): return self.__senha
    def get_endereco(self): return self.__endereco
    def get_nascimento(self): return self.__nascimento
    def get_contas(self): return self.__contas

    # Adiciona uma nova conta à lista de contas do cliente
    def add_conta(self, conta):
        self.__contas.append(conta)



    # ------------------- CLASSE ABSTRATA -------------------
    
    class OperacoesFinanceiras(ABC):
        # Define métodos abstratos s
        @abstractmethod
        def depositar(self, valor): pass

    @abstractmethod
    def sacar(self, valor): pass

    @abstractmethod
    def transferir(self, destino, valor): pass



    #  ------------------- CLASSE EXTRATO -------------------
    
    class Extrato:
        def __init__(self):
            # Guarda as transações feitas na conta
            self.__transacoes = []

    def registrar(self, tipo, valor, saldo):
        # Adiciona uma transação à lista (ex: depósito, saque, transferência)
        self.__transacoes.append({"tipo": tipo, "valor": valor, "saldo": saldo})

    def mostrar(self):
        # Exibe todas as transações feitas na conta
        print("Extrato:")
        for t in self.__transacoes:
            print(f"{t['tipo']}: R${t['valor']:.2f} | Saldo: R${t['saldo']:.2f}")



    #  ------------------- CLASSE BASE - CONTA -------------------
    
    class Conta(OperacoesFinanceiras):
        def __init__(self, numero, cliente, senha):
            # Cada conta tem um número, cliente associado, senha, saldo e extrato
            self.__numero = numero
            self.__cliente = cliente
            self.__senha = senha
            self.__saldo = 0.0
            self.__extrato = Extrato()

    # Getters para acessar dados protegidos
    def get_numero(self): return self.__numero
    def get_cliente(self): return self.__cliente
    def get_saldo(self): return self.__saldo
    def get_senha(self): return self.__senha

    def depositar(self, valor):
        # Verifica se o valor é válido
        if valor <= 0:
            print("Erro: valor deve ser positivo")
            return False
        # Atualiza o saldo e registra no extrato
        self.__saldo += valor
        self.__extrato.registrar("Depósito", valor, self.__saldo)
        print(f"Depósito de R${valor:.2f} realizado.")
        return True

    def transferir(self, destino, valor):
        # Realiza um saque e, se bem-sucedido, deposita no destino
        if self.sacar(valor):
            destino.depositar(valor)
            self.__extrato.registrar(
                f"Transferência p/ conta {destino.get_numero()}", valor, self.__saldo)
            print(f"Transferência de R${valor:.2f} realizada.")
            return True
        return False

    def mostrar_extrato(self):
        # Mostra todas as movimentações da conta
        print(f"\nExtrato da conta {self.__numero}:")
        self.__extrato.mostrar()


    #  ------------------- CLASSE CONTA CORRENTE -------------------
    
    class ContaCorrente(Conta):
        def sacar(self, valor):
            # Permite sacar qualquer valor disponível no saldo
            if valor > 0 and valor <= self.get_saldo():
                # Acessa o atributo privado da classe-mãe usando _Conta__
                self._Conta__saldo -= valor
                self._Conta__extrato.registrar("Saque", valor, self.get_saldo())
                print(f"Saque de R${valor:.2f} realizado.")
                return True
            print("Saldo insuficiente ou valor inválido.")
            return False


    
    # ------------------- CLASSE CONTA POUPANÇA -------------------
    
    class ContaPoupanca(Conta):
        # Define um saldo mínimo que deve permanecer na conta
        SALDO_MINIMO = 100.0

        def sacar(self, valor):
            # Só permite saque se o saldo após a retirada for maior que o mínimo
            if valor > 0 and (self.get_saldo() - valor) >= self.SALDO_MINIMO:
                self._Conta__saldo -= valor
                self._Conta__extrato.registrar("Saque", valor, self.get_saldo())
                print(f"Saque de R${valor:.2f} realizado.")
                return True
            print(f"Não é permitido sacar. Saldo mínimo R${self.SALDO_MINIMO:.2f}")
            return False

![Image](https://github.com/user-attachments/assets/ba2b7ec5-1107-4e15-813a-ff9b4e3f859c)


### Explicação do código por partes → ✩ funcion.py

    # Importa bibliotecas e classes especificadas 
    import os
    from classes import Banco, ContaCorrente, ContaPoupanca
    
    # Cria uma instância do banco — objeto principal que gerencia clientes e contas
    banco = Banco()
    
    
    #  ------------------- MENUS DO SISTEMA -------------------
    
    
    # Exibe o menu inicial de login/cadastro
    def menu_login():
        print("\n1- Cadastro de cliente\n2- Cadastro de conta\n3- Login\n0- Sair")
        try:
            # Retorna a opção escolhida pelo usuário convertida para número inteiro
            return int(input("---> "))
        except ValueError:
            # Evita erro caso o usuário digite letras em vez de números
            print("Entrada inválida. Digite apenas números para escolher uma opção.")
    
    # Menu para escolher o tipo de conta no login
    def menu_conta():
        print("\n1- Login Conta Corrente\n2- Login Conta Poupança\n0- Sair")
        try:
            return int(input("---> "))
        except ValueError:
            print("Entrada inválida. Digite apenas números para escolher uma opção.")
    
    # Menu principal com as operações disponíveis dentro da conta
    def menu_principal():
        print("\n1- Cadastrar outra conta\n2- Listar contas\n3- Depósito\n4- Saque\n5- Transferência\n6- Consultar saldo\n7- Extrato\n0- Sair")
        try:
            return int(input("---> "))
        except ValueError:
            print("Entrada inválida. Digite apenas números para escolher uma opção.")
    
  
    # ------------------- FUNÇÕES AUXILIARES -------------------
  
    
    # Função para cadastrar uma nova conta (corrente ou poupança)
    def cadastro_conta(cliente):
        try:
            tipo = int(input("Tipo de conta (1-Poupança, 2-Corrente): "))
        except ValueError:
            print("Entrada inválida. Digite apenas 1 ou 2 para escolher uma opção.")
            return None
    
    # Solicita a senha da conta
    senha = input("Senha da conta: ")

    # Gera automaticamente o número da conta com base na quantidade já existente
    numero = len(cliente.get_contas()) + 1

    # Cria a conta conforme o tipo escolhido
    if tipo == 1:
        conta = ContaPoupanca(numero, cliente, senha)
        print(f"Conta Poupança criada! Número: {numero}")
    elif tipo == 2:
        conta = ContaCorrente(numero, cliente, senha)
        print(f"Conta Corrente criada! Número: {numero}")
    else:
        # Caso o usuário digite um número fora do esperado
        print("Tipo inválido.")
        return None

    # Adiciona a conta criada à lista de contas do cliente
    cliente.add_conta(conta)
    return conta


    # Função para realizar login em uma conta existente
    def login_conta():
        try:
            # Solicita o número da conta e converte para inteiro
            numero = int(input("Número da conta: "))
        except ValueError:
            print("Número da conta deve conter apenas números.")
            return None

    # Solicita a senha
    senha = input("Senha: ")

    # Procura a conta e o cliente correspondente dentro do banco
    for cliente in banco.clientes.values():
        for conta in cliente.get_contas():
            if conta.get_numero() == numero and conta.get_senha() == senha:
                print(f"Login bem-sucedido! {cliente.get_nome()}")
                return conta  # Retorna o objeto conta se o login for válido

    # Caso não encontre uma conta correspondente
    print("Conta ou senha inválidos.")
    return None


    # Função para realizar um depósito
    def depositar(conta):
        try:
            valor = float(input("Valor do depósito: "))
        except ValueError:
            print("Valor inválido. Digite um número válido para realizar o depósito.")
            return
    
    # Chama o método da classe que faz o depósito no saldo
    conta.depositar(valor)


    # Função para realizar um saque
    def sacar(conta):
        try:
            valor = float(input("Valor do saque: "))
        except ValueError:
            print("Valor inválido. Digite um número válido para realizar o saque.")
            return
    
    # Chama o método da classe que executa o saque
    conta.sacar(valor)


    # Função para realizar transferência entre contas
    def transferir(conta):
        try:
            destino_num = int(input("Número da conta destino: "))
            valor = float(input("Valor da transferência: "))
        except ValueError:
            print("Entrada inválida. Digite apenas números para o número da conta e o valor.")
            return

    # Procura a conta de destino em todos os clientes cadastrados
    for cliente in banco.clientes.values():
        for c in cliente.get_contas():
            if c.get_numero() == destino_num:
                # Se a conta destino for encontrada, realiza a transferência
                conta.transferir(c, valor)
                return
    print("Conta destino não encontrada.")


    # Função simples para exibir o saldo atual da conta
    def consultar_saldo(conta):
        print(f"Saldo: R${conta.get_saldo():.2f}")
    
    
    # Função auxiliar que pausa o programa e limpa o terminal
    def LP():
        os.system('pause')  # Espera o usuário pressionar uma tecla
        os.system('cls')    # Limpa a tela do terminal 
    
![Image](https://github.com/user-attachments/assets/ba2b7ec5-1107-4e15-813a-ff9b4e3f859c)


### Explicação do código em partes → ✩ app.py

    # Importa todas as funções e classes do funcion.py e classes.py
    from funcion import *
    from classes import *
    
    # Dicionário que armazena os clientes cadastrados
    clientes = {}
    
    # Loop principal do programa (mantém o sistema rodando até o usuário escolher sair)
    while True:
        try:
            # Exibe o menu inicial e trata a opção escolhida pelo usuário
            match menu_login():
            
            # ------------------- OPÇÃO 1: CADASTRAR CLIENTE -------------------
            case 1:
                LP()  # Função que limpa a tela (deixa a interface mais limpa)
                try:
                    # Coleta os dados do cliente
                    nome = input("Nome completo: ")
                    cpf = int(input("CPF (somente números): "))
                    telefone = int(input("Telefone (somente números): "))
                    endereco = input("Endereço: ")
                    nascimento = input("Data de nascimento (DD/MM/AAAA): ")
                    senha = input("Senha: ")

                    # Chama o método do banco que cria e registra o cliente
                    banco.cadastrar_cliente(nome, cpf, telefone, senha, endereco, nascimento)

                except ValueError:
                    # Caso o usuário digite letras em campos numéricos (como CPF)
                    print("Erro no cadastro. CPF e telefone devem conter apenas números.")
                    continue  # Volta ao início do loop sem travar o programa
                LP()

            # ------------------- OPÇÃO 2: CADASTRAR CONTA -------------------
            case 2:
                LP()
                try:
                    # Pede o CPF do cliente para vincular a conta
                    cpf = int(input("CPF do cliente: "))
                except ValueError:
                    print("CPF deve conter apenas números.")
                    continue

                # Busca o cliente no banco de dados (dicionário de clientes)
                cliente = banco.clientes.get(cpf)
                if not cliente:
                    print("Cliente não encontrado.")
                    continue  # Volta ao menu principal se o cliente não existir

                # Cria uma nova conta associada ao cliente
                cadastro_conta(cliente)
                LP()

            # ------------------- OPÇÃO 3: LOGIN NA CONTA -------------------
            case 3:
                LP()
                try:
                    # Faz o login na conta (verifica número e senha)
                    conta = login_conta()
                except ValueError:
                    print("Número da conta deve conter apenas números.")
                    continue
                
                # Se o login falhar, volta para o menu principal
                if not conta:
                    continue

                LP()
                # Loop interno: menu de operações bancárias após login
                while True:
                    LP()
                    try:
                        # Exibe o menu de opções dentro da conta (depósito, saque, etc.)
                        match menu_principal():
                            
                            # ------------------- CADASTRAR OUTRA CONTA -------------------
                            case 1:
                                LP()
                                cadastro_conta(conta.get_cliente())  # Cria outra conta para o mesmo cliente
                                LP()

                            # ------------------- CONSULTAR CONTAS DO CLIENTE -------------------
                            case 2:
                                LP()
                                for c in conta.get_cliente().get_contas():
                                    print(f"Conta {c.get_numero()} | Saldo: R${c.get_saldo():.2f}")
                                LP()

                            # ------------------- DEPÓSITO -------------------
                            case 3:
                                LP()
                                depositar(conta)  # Função que adiciona saldo à conta
                                LP()

                            # ------------------- SAQUE -------------------
                            case 4:
                                LP()
                                sacar(conta)  # Retira dinheiro da conta
                                LP()

                            # ------------------- TRANSFERÊNCIA -------------------
                            case 5:
                                LP()
                                transferir(conta)  # Transfere valor para outra conta
                                LP()

                            # ------------------- CONSULTAR SALDO -------------------
                            case 6:
                                LP()
                                consultar_saldo(conta)  # Mostra o saldo atual
                                LP()

                            # ------------------- CONSULTAR EXTRATO -------------------
                            case 7:
                                LP()
                                conta.mostrar_extrato()  # Mostra o histórico de movimentações
                                LP()

                            # ------------------- SAIR DA CONTA -------------------
                            case 0:
                                LP()
                                print("Saindo...")
                                LP()
                                break  # Sai do loop interno (volta ao menu principal)

                            # ------------------- OPÇÃO INVÁLIDA -------------------
                            case _:
                                LP()
                                print("Opção inválida!")
                                LP()

                    # Captura erros de entrada (ex: usuário digita letra em vez de número)
                    except ValueError:
                        print("Entrada inválida. Digite apenas números válidos para escolher uma opção.")
                        LP()

            # ------------------- OPÇÃO 0: SAIR DO SISTEMA -------------------
            case 0:
                print("Obrigada por usar nosso banco!")
                LP()
                break  # Encerra o loop principal e finaliza o programa

            # ------------------- OPÇÃO INVÁLIDA (MENU PRINCIPAL) -------------------
            case _:
                print("Opção inválida!")
                LP()

    # Tratamento de erro caso alguma exceção aconteça fora dos blocos
    except ValueError:
        print("Entrada inválida. Tente novamente.")
