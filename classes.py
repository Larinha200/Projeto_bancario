
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
        saldo_atual = self.get_saldo()

        # Verifica se o saque deixará o saldo acima do mínimo
        if saldo_atual - valor >= self.SALDO_MINIMO:
            self._Conta__saldo -= valor
            self._Conta__extrato.registrar("Saque", valor, self.get_saldo())
            print(f"Saque de R${valor:.2f} realizado com sucesso!")
            return True
        else:
            print(f"Saque negado! É necessário manter saldo mínimo de R${self.SALDO_MINIMO:.2f}.")
            print(f"Saldo atual: R${saldo_atual:.2f}")
            return False
