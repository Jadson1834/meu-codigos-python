# # 1. Jogo da Adivinhação:

# # Objetivo: Adivinhar um número secreto.

# # Regras:

# # O jogador digita um número.
# # O programa informa se o chute é mais alto ou mais baixo que o número secreto.
# # O jogo continua até que o jogador adivinhe o número secreto.

import random
numeroSecreto = random.randint(0,100)

while True:
    numeroSelecionado = int(input("informe um numero:"))
    if numeroSelecionado == numeroSecreto:
        break
    elif numeroSelecionado >= numeroSecreto:
        print("o numero é menor")
    elif numeroSelecionado <= numeroSecreto:
        print("o numero é maior")

# 2. Tabuada Interativa:

# Objetivo: Gerar a tabuada de um número digitado pelo usuário.

# Regras:

# O usuário digita um número.
# O programa imprime a tabuada do número digitado.
# O usuário pode digitar outro número ou 0 para sair.

numeroEscolhido = int(input("selecione um numero: "))
numero = 1
while numero <= 10:
    resul = (numero * numeroEscolhido)
    print( f"{numeroEscolhido} . {numero} = {resul}")
    numero += 1
    if numeroEscolhido == 0:
        break

# 3. Contagem Regressiva:

# Objetivo: Fazer uma contagem regressiva a partir de um número digitado.

# Regras:

# O usuário digita um número.
# O programa imprime os números da contagem regressiva, começando pelo número digitado e terminando em 0.

numeroEscolhido = int(input("selecione um numero:"))

while numeroEscolhido >= 0:
    print(numeroEscolhido)
    numeroEscolhido -= 1
# 4. Simulador de Caixa Eletrônico:

# Objetivo: Simular um caixa eletrônico com as operações de saque, depósito e consulta de saldo.

# Regras:

# O usuário pode realizar as operações de saque, depósito ou consulta de saldo.
# O programa verifica se o valor do saque é superior ao saldo.
# O programa atualiza o saldo após cada operação.
# O usuário pode sair do simulador a qualquer momento.
menu = ('''
================ MENU ===============
opção [1] Saquar
opção [2] Depositar
opção [3] Saldo
opção [4] Sair'''
)
conta = 0
saldo = 0
print(menu)

while True:
    escolha = int(input('escolha:'))
    if escolha == 1:
        saque = int(input('deseja saquar quanto:'))
        if saque > 0 and saque < conta:
            conta -= saque
        else:
            print('erro, seu saque é maior que o saldo')
    if escolha == 2:
        deposito = int(input('deseja depositar quanto:'))
        if deposito > 0:
           conta +=  deposito
    if escolha == 3:
       print (f'sua conta tem r${conta:.2f}')
    if escolha == 4:
        break

# 5. Jogo de Adivinhação de Palavras:

# Objetivo: Adivinhar uma palavra secreta dentre uma lista de opções.

listaSecreta = ["carelos","mateus","banana","video-game"]

while True:
    nomeEscolhido = input("escolha uma palavra: ")
    if nomeEscolhido in listaSecreta:
        break
