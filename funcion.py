
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

