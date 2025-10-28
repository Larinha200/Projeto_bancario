from classess import *

def menu_login():
    print("1- Cadastro de cliente \n2- Cadastro de conta \n3- Login \n0- sair")
    resposta_login = int(input("--->"))
    return resposta_login

def menu_conta():
    print("1- Login na conta corrente \n2-Login na conta poupança  \n0- Sair")
    resposta_conta = int(input("--->"))
    return resposta_conta
    
def menu_principal():
    print("1- Cadastrar outra conta \n2- Contas \n3- Depósito \n4- Saque \n5- Tranferência entre contas \n6- Consulta de saldo \n7- Consulta de extrato \n0- Sair ")
    resposta_principal = int(input("--->"))
    return resposta_principal

def menu_contas():
    print("1- Poupança \n2-Corrente")
    resposta_contas = int(input("--->"))
    return resposta_contas

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

def cadastro_conta():
    cpf_cliente = int(input("CPF:"))
    pass

def login_cliente(clientes):
    while True:
        print("\n=== LOGIN ===")
        cpf = int(input("Digite seu CPF: "))
        
        try:
            # Verifica se o cliente existe
            cliente = clientes.get(cpf)
            if not cliente:
                print(" CPF não encontrado. Faça o cadastro primeiro.")
            
            else:
                print("Usuario encontrado, insira sua senha")
                
                while True:
                    senha = input("------> ")
                    if cliente.getSenha() != senha:
                        print(" Senha incorreta.")
                    else:
                        print("senha correta")
                        print(f"\n Login realizado com sucesso! Bem-vindo(a), {cliente.getNome()}!")
                        break
                break
        except:
             pass