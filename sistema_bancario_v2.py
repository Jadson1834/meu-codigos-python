def menu():
  print("""
  ================== Menu =======================
  1 - Criar usuário
  2 - Criar Conta
  3 - Sacar
  4 - Depósito          
  5 - Exibir extrato
  6 - Listar contas
  7 - Sair
  """)
  return int(input("O que deseja fazer? "))

def sacar(saldo, valor, extrato, limite, numero_saque, limite_saque):
  excedeu_limite = valor > limite
  excedeu_saldo = valor > saldo
  excedeu_saque = numero_saque >= limite_saque

  if excedeu_limite:
      print("Valor muito alto")
  elif excedeu_saldo:
      print("Excedeu o saldo")
  elif excedeu_saque:
      print("Excedeu o número de saques")
  elif valor > 0:
      saldo -= valor
      extrato += f"Saque:\t\tR${valor:.2f}\n"
      numero_saque += 1
      print("Saque realizado com sucesso")
  else:
      print("Operação deu errado, tente novamente")

  return saldo, extrato, numero_saque

def depositar(saldo, valor, extrato):
  if valor > 0:
      saldo += valor
      extrato += f"Depósito:\t\tR${valor:.2f}\n"
  else:
      print("Operação deu erro, tente novamente")
  return saldo, extrato

def exibir_extrato(saldo, extrato):
  print(extrato if extrato else "Não há movimentação no extrato")
  print(f"Seu saldo: \t\tR${saldo:.2f}")

def filtar_usuario(cpf, usuarios):
  for usuario in usuarios:
      if usuario["cpf"] == cpf:
          return usuario
  return None

def criar_usuario(usuarios):
  cpf = input("Informe seu CPF (somente números): ")
  usuario = filtar_usuario(cpf, usuarios)
  if usuario:
      print("Já existe um usuário com esse CPF")
      return
  nome = input("Me fale seu nome completo: ")
  data_nascimento = input("Me fale sua data de nascimento (dd-mm-aaaa): ")
  endereco = input("Me fale seu endereço (logradouro, nro - bairro - cidade/sigla estado): ")

  usuarios.append({
      "cpf": cpf,
      "nome": nome,
      "data_nascimento": data_nascimento,
      "endereco": endereco
  })

  print("Usuário criado com sucesso")

def criar_conta(agencia, numero_conta, usuarios):
  cpf = input("Informe o CPF do usuário: ")
  usuario = filtar_usuario(cpf, usuarios)

  if usuario:
      print("\nConta criada com sucesso")
      return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
  print("\nUsuário não encontrado")

def listar_contas(contas):
  for conta in contas:
      linha = f"""
      Agencia:\t{conta["agencia"]}
      C/C:\t\t{conta["numero_conta"]}
      Titular:\t{conta["usuario"]["nome"]}
      """
      print(linha)
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
      if opcao == 1:
          criar_usuario(usuarios)

      elif opcao == 2:
          numero_conta = len(contas) + 1
          conta = criar_conta(AGENCIA, numero_conta, usuarios)
          if conta:
              contas.append(conta)

      elif opcao == 3:
          valor = float(input("Informe o valor do saque: "))
          saldo, extrato, numero_saque = sacar(saldo, valor, extrato, limite, numero_saque, LIMITE_SAQUE)

      elif opcao == 4:
          valor = float(input("Digite o valor do depósito: "))
          saldo, extrato = depositar(saldo, valor, extrato)

      elif opcao == 5:
          exibir_extrato(saldo, extrato)

      elif opcao == 6:
          listar_contas(contas)

      elif opcao == 7:
          break

      else:
          print("Operação inválida, selecione novamente a operação desejada")

main()
