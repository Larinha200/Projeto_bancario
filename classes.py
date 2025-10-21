from abc import ABC, abstractmethod #importar a biblioteca ABC

#criação das classes 
class Cliente:

    def __init__(self, nome: str, cpf:int, telefone:int, senha: str, endereço:str, id:0, nascimento:int):
        self.__id = id
        self.__nome = nome
        self.__cpf = cpf
        self.__telefone = telefone
        self.__endereço = endereço
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
        return self.__endereço
    
    def getNascimento(self):
        return self.__nascimento
    
    #Def para adicionar conta
    def add_conta(self, conta):
        return self.__contas.append(conta)
    
    def cadastrar_cliente(self,nome, cpf, telefone,  senha, endereco, nascimento, clientes):
        novo_cliente = Cliente(nome, cpf, telefone, senha, endereco, nascimento)
        clientes[novo_cliente.getId()] = novo_cliente
        return novo_cliente

class OperacoesFinanceiras(ABC):
    pass

class Conta(OperacoesFinanceiras, ABC):
    def __init__(self, numero: int, cliente: Cliente):
        self.__numero = numero


class Extrato:
    pass

class ContaCorrente(Conta):
    pass

class ContaPoupanca(Conta):
    pass

class Banco:
    pass