from abc import ABC, abstractmethod #importar a biblioteca ABC

#criação das classes 
class Banco:
    pass

class Conta(ABC):
    pass

class Cliente(Conta, ABC):

    def __init__(self, nome: str, cpf:int, telefone:int, senha: str, endreço:str, id:0):
        self.__id = id
        self.__nome = nome
        self.__cpf = cpf
        self.__telefone = telefone
        self.__endereço = endreço
        self.__senha = senha
        self.__contas = []

#GETS para acessar atributos privados da classe cliente
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
    
    #Def para adicionar conta
    def add_conta(self, conta):
        return self.__contas.append(conta)
    
    def cadastro(nome, cpf,telefone, endereço, senha, id):
        id +=1
        cliente= Cliente(nome,cpf, telefone, endereço,senha)
        return cliente


class Extrato:
    pass

class ContaCorrente(Conta):
    pass

class ContaPoupanca(Conta):
    pass
