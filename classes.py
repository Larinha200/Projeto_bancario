from abc import ABC, abstractmethod #importar a biblioteca ABC

#criação das classes 
class Cliente:

    def __init__(self, nome: str, cpf:int, telefone:int, senha: str, endereco:str,nascimento:int, id:0 ):
        self.__id = id
        self.__nome = nome
        self.__cpf = cpf
        self.__telefone = telefone
        self.__endereco = endereco
        self.__nascimento = nascimento
        self.__senha = senha
        self.__contas = []

#GETS para acessar atributos privados da classe cliente
    def getId(self):
        return self.__id
    
    def getNome(self):
        return self.__nome
    
    def getCpf(self):
        return self.__cpf
    
    def getContas(self):
        return self.__contas
    
    def getTelefone(self):
        return self.__telefone
    
    def getSenha(self):
        return self.__senha 
    
    def getEndereco(self):
        return self.__endereco
    
    def getNascimento(self):
        return self.__nascimento
    
    #Def para adicionar conta
    def add_conta(self, conta):
        return self.__contas.append(conta)
    
    @staticmethod #indica que não é preciso criar um objeto da classe para usar o método.
    def cadastrar_cliente(nome, cpf, telefone,  senha, endereco, nascimento,id, clientes):
        novo_cliente = Cliente(nome, cpf, telefone, senha, endereco, nascimento,id)
        clientes[novo_cliente.getId()] = novo_cliente
        return novo_cliente

class OperacoesFinanceiras(ABC):
    @abstractmethod
    def depositar(self, valor: float):
        pass

    @abstractmethod
    def sacar(self, valor: float):
        pass

    @abstractmethod
    def transferir(self, destino, valor: float):
        pass
    
    
class Extrato:
    pass

class Conta(OperacoesFinanceiras):
    def __init__(self, numero: int, cliente: Cliente):
        self.__numero = numero
        self.__cliente = cliente
        self.__saldo = 0.0
        self.__extrato = Extrato()
    
    #GETS para acessar atributos privados da classe conta
    def getNumero(self):
        return self.__numero

    def getCliente(self):
        return self.__cliente
    
    def getSaldo(self):
        return self.__saldo

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
            print("Valor de depósito inválido.")

    #metodo abstrato para sacar
    @abstractmethod
    def sacar(self, valor: float):
        pass

    #transferir saldo para uma conta
    def transferir(self, destino, valor: float):
        if self.sacar(valor):
            destino.depositar(valor)
            self.__extrato.registrar(f"Transferência para conta {destino.numero}", -valor, self.__saldo)
            destino.Conta__extrato.registrar(f"Transferência recebida de conta {self.__numero}", valor, destino.saldo)
            return True
        return False

    # Sobrecarga de método para consultar saldo da conta
    def consultar_saldo(self, formatado: bool = False):
        if formatado:
            return f"Saldo da conta {self.__numero}: R${self.__saldo:.2f}"
        else:
            return self.__saldo


class ContaCorrente(Conta):
    pass

class ContaPoupanca(Conta):
    pass

class Banco:
    pass