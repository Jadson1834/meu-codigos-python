# Desafio 1: Trocar Valores
# Escreva um programa que troque os valores de duas variáveis utilizando tuplas. Por exemplo, se a = 10 e b = 5, após a troca, a deverá ser 5 e b deverá ser 10.
a = 10
b = 5
valor = (a,b)
valores = list(valor)
valores[0] = 5
valores[1] = 10
print(valores)

# Desafio 2: Calculadora Simples
# Crie uma calculadora simples que aceite dois números e um operador (como "+", "-", "*", "/") como entrada e retorne o resultado. Utilize tuplas para armazenar os valores de entrada.
numero = []
num1 = int(input("me fale um numero: "))
num2 = int(input("me fale um numero: "))
operador = input("me fale um operador: ")

if operador  == "+":
    soma = num1 + num2
    print(f"o resultado dessa soma é {soma}")
elif operador  == "-":
    subtracao = num1 - num2
    print(f"o resultado dessa subtracao é {subtracao}")
elif operador  == "*":
    multi = num1 * num2
    print(f"o resultado dessa multiplicaçao é {multi}")
elif operador  == "/":
    divisao = num1 / num2
    print(f"o resultado dessa divisao é {divisao}")

numero.append(num1)
numero.append(num2)
numeros = tuple(numero)
print(numeros)

# Desafio 3: Média de Notas
# Escreva um programa que calcule a média de três notas de um aluno. As notas devem ser fornecidas como entrada pelo usuário e armazenadas em uma tupla.
nota = []
nota1 = int(input("me fale sua nota: "))
nota2 = int(input("me fale sua nota: "))
nota3 = int(input("me fale sua nota: "))

nota.append(nota1)
nota.append(nota2)
nota.append(nota3)
notas = tuple(nota)
print (notas)
media = (nota1 + nota2 + nota3)/4
print(media)

# Desafio 4: Conversão de Temperaturas
# Crie um programa que converta uma temperatura de Celsius para Fahrenheit e vice-versa. Utilize tuplas para armazenar a temperatura e a unidade de medida (Celsius ou Fahrenheit).
temperatura = []
temperatura_convertida = []
def converter_temperatura(Celsius,Fahrenheit):
    Celsius_para_Fahrenheit = (Celsius - 32)//1.8
    Fahrenheit_para_Celsius = (Fahrenheit * 1.8) + 32
    temperatura.append(f"{Celsius}°C")
    temperatura.append(f"{Fahrenheit}°F")
    temperatura_convertida.append(f"{Celsius_para_Fahrenheit}°F")
    temperatura_convertida.append(f"{Fahrenheit_para_Celsius}°C")
    
converter_temperatura(145,18)
print(temperatura)
print(temperatura_convertida)
temperaturas = tuple(temperatura)
temperatura_convertidas = tuple(temperatura_convertida)
print(temperaturas)
print(temperatura_convertidas)
