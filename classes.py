from abc import ABC, abstractmethod #importar a biblioteca ABC

#criação das classes 
class Banco:
    def __init__(self):
         pass
    
    novo_cliente= {}# Dicionário para guardar os clientes do banco
    
    @staticmethod
    def cadastrar_cliente(nome, cpf, telefone, senha, endereco, nascimento, clientes):
        # Se CPF já cadastrado, mostra aviso e retorna o cliente existente
        if cpf in clientes:
            print(f"\n Já existe um cliente com o CPF {cpf} cadastrado!")
            return clientes[cpf]

        # Cria e adiciona novo cliente ao dicionario
        novo_cliente = Cliente(nome, cpf, telefone, senha, endereco, nascimento)
        clientes[cpf] = novo_cliente
        return novo_cliente
    
    def listar():
        pass

    def criar_poupanca():
        pass

    def criar_corrente():
        pass
        


class Cliente(Banco):
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
        super().__init__() # chama o construtor da classe "Banco"
        

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
        self.__transacoes.append({
            'tipo': tipo, # Tipo da transação (depósito, saque, etc.)
            'valor': valor, # Valor da transação
            'saldo': saldo # Saldo atual após a transação
        })

    #Exibe todas as transações registradas no extrato
    def mostrar(self):
        # .2f significa que pode ter dois caracteres depois da virgula
        for transacao in self.__transacoes:
            return (f"{transacao['tipo']}: R${transacao['valor']:.2f} | Saldo: R${transacao['saldo']:.2f}")


class Conta(OperacoesFinanceiras):
    def __init__(self, numero: int, cliente: Cliente, senha: str):
        self.__numero = numero
        self.__cliente = cliente
        self.__senha = senha  # ← Nova senha da conta
        self.__saldo = 0.0
        self.__extrato = Extrato()
        super().__init__()
    
    #GETS para acessar atributos privados da classe conta
    def getNumero(self):
        return self.__numero

    def getCliente(self):
        return self.__cliente
    
    def getSaldo(self):
        return self.__saldo

    def getConta(self):
        return self.__conta
    
    def getSenha(self):
        return self.__senha
    

    #mostrar extrato da conta
    def mostrar_extrato(self):
        print(f"Extrato da conta {self.__numero}:")
        self.__extrato.mostrar()

    #depositar, somente se o saldo for maior que 0
    def depositar(self, valor: float):
        if valor > 0:
            self.__saldo += valor
            self.__extrato.registrar("Depósito", valor, self.__saldo)
        else:
            ("Valor de depósito inválido.")


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


class ContaPoupanca(Conta):
    def __init__(self, numero, cliente, senha):
        self.__senha = senha
        super().__init__( numero, cliente, senha)
        
    def getSenha(self):
        return self.__senha

    SALDO_MINIMO = 100.0

    #sacar por saldo minimo na conta
    def sacar(self, valor: float):
        if valor > 0 and (self.__saldo - valor) >= self.SALDO_MINIMO:
            self.__Conta_saldo -= valor
            self.__Conta_extrato.registrar("Saque", valor, self.__saldo)
            return True
        else:
            (f"Não é permitido sacar. Saldo mínimo de R$ {self.SALDO_MINIMO:.2f} deve ser mantido.")
            return False
