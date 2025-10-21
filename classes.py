from abc import ABC, abstractmethod #importar a biblioteca ABC

#criação das classes 
class Banco:
    pass

class Conta(ABC):
    pass

class Cliente(Conta, ABC):
    def __init__(self, nome: str, cpf):
        self.__nome = nome
        self.__cpf = cpf
        self.__contas = []

    def cadastro():
        pass

#GETS para acessar atributos privados da classe cliente
    def getNome(self):
        return self.__nome
    
    def getCpf(self):
        return self.__cpf
    
    def getContas(self):
        return self.__contas
    
    #Def para adicionar conta
    def add_conta(self, conta):
        return self.__contas.append(conta)


class Extrato:
    pass

class ContaCorrente(Conta):
    pass

class ContaPoupanca(Conta):
    pass
