
from classes import Banco, ContaCorrente, ContaPoupanca

banco = Banco()

def menu_login():
    print("\n1- Cadastro de cliente\n2- Cadastro de conta\n3- Login\n0- Sair")
    try:
        return int(input("---> "))
    except ValueError:
        print("Entrada inválida. digite apenas números para escolher uma opção.")

def menu_conta():
    print("\n1- Login Conta Corrente\n2- Login Conta Poupança\n0- Sair")
    try:
        return int(input("---> "))
    except ValueError:
        print("Entrada inválida. digite apenas números para escolher uma opção.")

def menu_principal():
    print("\n1- Cadastrar outra conta\n2- Listar contas\n3- Depósito\n4- Saque\n5- Transferência\n6- Consultar saldo\n7- Extrato\n0- Sair")
    try:
        return int(input("---> "))
    except ValueError:
        print("Entrada inválida. digite apenas números para escolher uma opção.")

# Funções auxiliares
def cadastro_conta(cliente):
    try:
        tipo = int(input("Tipo de conta (1-Poupança, 2-Corrente): "))
    except ValueError:
        print("Entrada inválida. digite apenas 1 ou 2 para escolher uma opção.")
        return None
    
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
    try:
        numero = int(input("Número da conta: "))
    except ValueError:
        print("Número da conta deve conter apenas números.")
        return None
    senha = input("Senha: ")
    
    for cliente in banco.clientes.values():
        for conta in cliente.get_contas():
            if conta.get_numero() == numero and conta.get_senha() == senha:
                print(f"Login bem-sucedido! {cliente.get_nome()}")
                return conta
    print("Conta ou senha inválidos.")
    return None

def depositar(conta):
    try:
        valor = float(input("Valor do depósito: "))
    except ValueError:
        print("Valor inválido. Digite um número válido para realizar o depósito.")
        return
    conta.depositar(valor)

def sacar(conta):
    try:
        valor = float(input("Valor do saque: "))
    except ValueError:
        print("Valor inválido. Digite um número válido para realizar o saque.")
        return
    conta.sacar(valor)

def transferir(conta):
    try:
        destino_num = int(input("Número da conta destino: "))
        valor = float(input("Valor da transferência: "))
    except ValueError:
        print("Entrada inválida. Digite apenas números para o número da conta e o valor.")
        return
    
    for cliente in banco.clientes.values():
        for c in cliente.get_contas():
            if c.get_numero() == destino_num:
                conta.transferir(c, valor)
                return
    print("Conta destino não encontrada.")

def consultar_saldo(conta):
    print(f"Saldo: R${conta.get_saldo():.2f}")

