from classes import *

def menu_login():
    print("1- Cadastro \n2- Login na conta corrente \n3- Login na conta poupança")
    resposta_login = int(input("--->"))
    return resposta_login
    
def menu_principal():
    print("1- Cadastro \n3- Contas \n4- Depósito \n5- Saque \n6- Tranferência entre contas \n7- Conslta de saldo \n8- Consulta de extrato ")

def menu_cadastro():
    print("\n=== CADASTRO DE CLIENTE ===")
    nome = input("Nome completo: ")
    cpf = int(input("CPF (somente números): "))
    telefone = int(input("Telefone (somente números): "))
    endereco = input("Endereço: ")
    senha = input("Senha: ")

    cliente = cadastrar_cliente(nome, cpf, telefone, endereco, senha, clientes)
    return cliente