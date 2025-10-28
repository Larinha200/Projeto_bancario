from classes import *

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
        print("\n Nenhum cliente cadastrado ainda.\n")
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



def login_cliente(clientes):
    while True:
        print("\n=== LOGIN ===")
        cpf = int(input("Digite seu CPF: "))
        
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

def cadastro_conta(clientes):
    print("\n=== CADASTRO DE CONTA ===")
    cpf_cliente = int(input("CPF do cliente: "))

    # Verificar se o cliente está cadastrado
    cliente = clientes.get(cpf_cliente)
    if not cliente:
        print("Cliente não encontrado. Faça o cadastro primeiro.")
        return

    tipo = int(input("Digite o tipo de conta (1 - Poupança | 2 - Corrente): "))
    senha = input("Defina uma senha para esta conta: ")  # ← Nova parte

    # Gerar número de conta
    numero_conta = len(cliente.getConta()) + 1  

    if tipo == 1:
        conta = ContaPoupanca(numero_conta, cliente, senha)
        print(f" Conta Poupança criada com sucesso! Número: {numero_conta}")
    elif tipo == 2:
        conta = ContaCorrente(numero_conta, cliente, senha)
        print(f"Conta Corrente criada com sucesso! Número: {numero_conta}")
    else:
        print("Tipo de conta inválido.")
        return

    # Vincular conta ao cliente
    cliente.add_conta(conta)
    print(f"Conta vinculada ao cliente {cliente.getNome()} ({cliente.getCpf()}).")

def login_conta(clientes):
    conta_corrente = ContaCorrente.getSenha()
    conta_poupanca = ContaPoupanca.getSenha()
    match menu_conta():
        case 1:
            while True:
                print("\n LOGIN NA CONTA")
                cpf = int(input("Digite seu CPF: "))

                # Verifica se o cliente existe
                cliente = clientes.get(cpf)
                if not cliente:
                    print(" Cliente não encontrado. Faça o cadastro primeiro.")
                
                else:
                    print("cliente encontrado, insira senha da conta ")
                    senha = input("------> ")
                    if conta_corrente.getSenha() != senha:
                        print(" Senha incorreta.")
                    else:
                        print("senha correta")
                        print(f"\n Login realizado com sucesso! Bem-vindo(a), {cliente.getNome()}!")
                        break
                        continue

            # Se o cliente tem contas cadastradas
            contas = cliente.getConta()
            if not contas:
                print(" Nenhuma conta encontrada para este cliente.")
             
            else:

                print(f"\nCliente {cliente.getNome()} possui {len(contas)} conta(s):")
                for chave, valor in contas.itens():
                    print(f'{chave}-{valor}')

                