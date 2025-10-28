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

#def menu_contas():
    print("1- Poupança \n2-Corrente")
    resposta_contas = int(input("--->"))
    return resposta_contas

def menu_cadastro(clientes):
    print("\nCadastro de cliente")
    nome = input("Nome completo: ")
    cpf = int(input("CPF (somente números): "))
    telefone = int(input("Telefone (somente números): "))
    endereco = input("Endereço: ")
    nascimento = input("Data de nascimento (DD/MM/AAAA): ")
    senha = input("Senha: ")
    cliente = Banco.cadastrar_cliente(nome, cpf, telefone, senha, endereco, nascimento, clientes)
    return cliente

#usado para testes 
def listar_clientes(clientes):
    if not clientes:
        print("\n Nenhum cliente cadastrado ainda.\n")
        return

    print("\nLista de clientes")
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
        print("\nLogin")
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
    print("\nCadastro conta")
    cpf_cliente = int(input("CPF do cliente: "))

    # Verificar se o cliente está cadastrado
    cliente = clientes.get(cpf_cliente)
    if not cliente:
        print("Cliente não encontrado. Faça o cadastro primeiro.")
        return

    tipo = int(input("Digite o tipo de conta \n1 - Poupança \n2 - Corrente \n----> "))
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
    while True:
        print("\nLogin da conta")

        numero = int(input("Digite o número da conta: "))
        senha = input("Digite a senha da conta: ")

        # Percorre todos os clientes
        for cliente in clientes.values():
            contas = cliente.getConta()
            # Percorre as contas de cada cliente
            for conta in contas:

                if conta.getNumero() != numero or conta.getSenha() != senha:
                    # Se não encontrar nenhuma conta correspondente
                    print("Número de conta ou senha incorretos.")
            
                else:
                    print(f"\nLogin bem-sucedido! Bem-vindo(a), {cliente.getNome()}.")
                    break
                      # retorna o objeto da conta logada
                 
            

def depositar(cliente):
    contas = cliente.getConta()
    
    if not contas:
        print("Este cliente não possui contas cadastradas.")
        return
    
    print("\ncontas ")
    for conta in contas:
        print(f"Conta {conta.getNumero()} | Saldo: R${conta.getSaldo():.2f}")
    try:
        numero = int(input("Digite o número da conta para depósito: "))
    except ValueError:
        print("Entrada inválida.")
        return
    
    conta_escolhida = None
    
    for conta in contas:
        if conta.getNumero() == numero:
            conta_escolhida = conta
            break
    
    if not conta_escolhida:
        print("Conta não encontrada.")
        return
    try:
        valor = float(input("Digite o valor do depósito: "))
    except ValueError:
        print("Valor inválido.")
        return
    
    if conta_escolhida.depositar(valor):  # Chama o método da classe
        print(f"Saldo atual: R${conta_escolhida.getSaldo():.2f}")
