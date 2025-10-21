from classes import *

def menu_login():
    print("1- Cadastro \n2- Login na conta corrente \n3- Login na conta poupança")
    resposta_login = int(input("--->"))
    return resposta_login
    
def menu_principal():
    print("1- Cadastro \n2- Contas \n3- Depósito \n4- Saque \n5- Tranferência entre contas \n6- Consulta de saldo \n7- Consulta de extrato ")

def menu_cadastro(clientes):
    print("\n=== CADASTRO DE CLIENTE ===")
    nome = input("Nome completo: ")
    cpf = int(input("CPF (somente números): "))
    telefone = int(input("Telefone (somente números): "))
    endereco = input("Endereço: ")
    nascimento = input("Data de nascimento (DD/MM/AAAA): ")
    senha = input("Senha: ")
    cliente = Banco.cadastrar_cliente(nome, cpf, telefone, senha, endereco, nascimento, clientes)
    return cliente
    
   

def listar_clientes(clientes):
    if not clientes:
        print("\n⚠️ Nenhum cliente cadastrado ainda.\n")
        return

    print("\n=== LISTA DE CLIENTES CADASTRADOS ===")
    for _, cliente in clientes.items():
        print(f"\nID: {cliente.getId()}")
        print(f"Nome: {cliente.getNome()}")
        print(f"CPF: {cliente.getCpf()}")
        print(f"Telefone: {cliente.getTelefone()}")
        print(f"Endereço: {cliente.getEndereco()}")
        print(f"Nascimento: {cliente.getNascimento()}")
        print(f"Senha: {cliente.getSenha()}")
        print("-" * 40)
