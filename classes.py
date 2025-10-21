from abc import ABC, abstractmethod #importar a biblioteca ABC

#criação das classes 
class Banco:
    pass

class Cliente:
    pass

class Conta(ABC):
    pass

class Extrato:
    pass

class ContaCorrente(Conta):
    pass

class ContaPoupanca(Conta):
    pass

