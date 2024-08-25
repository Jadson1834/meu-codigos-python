def menu():
    menu = print("""
    ================== Menu =======================
    1 - Criar usuario
    2 - Criar Conta
    3 - Sacar
    4 - Deposito          
    5 - Exibir extrato
    6 - Listar conta
    7 - sair
    """)
    return input(menu)

def sacar(*,saldo,valor,extrato,limite,numero_saque,limite_saque):
    excedeu_limite = valor > limite
    excedeu_saldo = valor > saldo
    excedeu_saque = numero_saque > limite_saque

    if excedeu_limite:
        print("valor muito alto")
    elif excedeu_saldo:
        print("excedeu o saldo")
    elif excedeu_limite:
        print("excedeu o numero de saques")
    elif valor > 0:
        saldo -= valor
        extrato += f"saque:\t\tR${valor:.2f}"
        numero_saque += 1
        print("saque realizado com sucesso")
    else:
        print("operaçao deu errado tente novamente")

        return saldo,extrato

def depositar(saldo,valor,extrato,/):
    if valor > 0:
        saldo += valor
        extrato += f"deposito:\t\t R${valor:.2f}"
    else:
        print("operaçao deu erro , tente novamente")
    return saldo,extrato

def exibir_extrato(saldo,/,*,extrato):
    print("nao tem movimentaçao no extrato" if not extrato else extrato)
    print(f"seu saldo: \t\t R${saldo:.2f}")

def filtar_usuario(cpf,usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_usuario(usuarios):
    cpf = input("informe seu cpf (somente numeros):")
    usuario = filtar_usuario(cpf,usuarios)
    if usuario:
        print("ja existe um usuario com esse CPF")
        return
    nome = input("me fale seu nome cpmpleto")
    data_nascimento = input("me fale sua data de nascimento (dd-mm-aaaa):")
    endereco = input("me fale seu endereço (logradouro,nro - bairo - cidade/sigla estado):")

    usuarios.append({"nome":nome,"data_nascimento":data_nascimento,"endereco":endereco})

    print("usuario criado com sucesso")

def criar_conta(agencia,numero_conta,usuarios):
    cpf = input("informe o cpf do usuario")
    usuario = filtar_usuario(cpf,usuarios)

    if  usuarios:
        print("\nconta criada com sucesso")
        return {"agencia":agencia,"numero_conta":numero_conta,"usuario":usuario}
    print("\nusuario nao encontrado")

def listar_contas(contas):
    for conta in contas:
        linha = f"""
            Agencia:\t{conta["agencia"]}
            C/C:\t\t{conta["numero_conta"]}
            Titular:\n{conta["usuario"]["nome"]}
"""
        print("=" * 100)

def main():
    LIMITE_SAQUE = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    numero_saque = 0
    extrato = ""
    usuarios = []
    contas = []

    while True:
        opcao = menu()
        if opcao == "1":
            criar_usuario(usuarios)

        elif opcao == 2:
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA,numero_conta,usuarios)
            if conta:
                contas.append(conta)

        elif opcao == 3:
            sacar()
        
        elif opcao == 4:
            depositar()

        elif opcao == 5:
            exibir_extrato()

        elif opcao == 6:
            listar_contas()

        elif opcao == 7:
             break
        
        else:
            print("operaçao invalida,selecione denovo a operaçao desejada")
