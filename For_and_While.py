# Desafios com While:
# Imprimir números de 1 a 10:
numero = 1
while numero <= 10:
    print(numero)
    numero += 1

# Imprimir números pares de 0 a 20:
numero = 0
while numero <= 20:
    numero += 1
    if numero %2 == 0:
        print(numero)

# Somar números de 1 a 100:
numero = 0
numeros = []
while numero <= 99:
    numero += 1
    numeros.append(numero)
    total = sum(numeros)
    print(total)

# Desafios do For com range:
# . Imprimir números de 1 a 10:
for numero in range(1,11):
    print(numero)

# Calcular a soma dos números de 1 a 100:
numeros = []
for numero in range(1,101):
    numeros.append(numero)
    soma = sum(numeros)
print(f"A soma dos números de 1 a 100 é: {soma}")


# Criar uma lista de números pares de 1 a 20:
pares = []
for numero in range(1,21):
    if numero %2 == 0:
        pares.append(numero)
        print (pares)
        
# Imprimir a tabuada de um número:
numeroEscolhido = int(input("escolha um numero:"))

for numero in range(1,11):
    tabuada = numeroEscolhido * numero
    print(tabuada)
# Calcular a média de 5 números:
numeros = []
for numero in range(1,6):
    numeros.append(numero)
    media = sum(numeros)/5
    print(media)

# Desafios do for simples
# Dada uma lista de números, some todos os elementos da lista e exiba o resultado.
numeros = [6,7,4,7,2,8]
soma = sum(numeros)
print(soma)

# Dada uma string e uma letra específica, conte quantas vezes essa letra aparece na string.
string = "clodoaldo"
print(string.count('a'))

# Dada uma lista de números, imprima apenas os números pares.
numeros = [0,3,4,2,7,8,6,463,63,6,57,53,54,213,65,67,67,56,5435,34]
for pares in numeros:
    if pares %2 == 0:
        print(pares)

# Dada uma lista de números, crie uma nova lista contendo os quadrados desses números.
numeros = [1,5,6,3,1,9,4,2,5,8]
for quadrados in numeros:
    if quadrados**2:
        print(quadrados**2)
