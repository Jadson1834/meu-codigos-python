# Criando uma Classe Simples
# Crie uma classe chamada Pessoa com um construtor __init__ que recebe o nome e a idade de uma pessoa. Em seguida, crie um objeto dessa classe com o nome "Alice" e a idade 25 e exiba os valores dos atributos.
class pessoa:
    def __init__(self,nome,idade):
        self.nome = nome
        self.idade = idade

alice = pessoa("Alice",25)
# Adicionando Métodos à Classe
# Adicione um método chamado saudacao à classe Pessoa que exiba uma saudação com o nome da pessoa. Crie um objeto e chame o método.
class pessoa():    
    def __init__(self,nome,idade):
        self.nome = nome
        self.idade = idade

    def apresentar(self):
        print(f"seu nome é {self.nome} e minha idade é {self.idade}")

alice = pessoa("Alice",25)
alice.apresentar()

# Classe Conta Bancária
# Crie uma classe ContaBancaria com os atributos saldo e titular. Adicione métodos para depositar e sacar dinheiro da conta. Crie um objeto da classe e realize algumas operações.
class conta_bancaria():
    def __init__(self,saldo,titular):
        self.saldo = saldo
        self.titular = titular

    def depositar(self,deposito):
        self.deposito = deposito
        self.saldo += self.deposito
        print(self.saldo)

    def saque(self,sacar):
        self.sacar = sacar
        self.saldo -= self.sacar
        print(self.saldo)
marcos = conta_bancaria(55,"nado")
marcos.depositar(50)
 marcos.saque(70)
# Classe Retângulo
# Crie uma classe Retangulo com os atributos largura e altura. Adicione um método chamado area que calcula a área do retângulo (largura * altura). Crie um objeto da classe e calcule sua área.
class retangulo():
    def __init__(self,largura,altura):
        self.largura = largura
        self.altura = altura

    def calcular_area(self):
        area = self.largura * self.altura
        print (area)

retangul = retangulo(8,8)
retangul.calcular_area()
