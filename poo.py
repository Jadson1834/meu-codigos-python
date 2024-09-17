# Faça um programa que cadastre clientes(nome, endereço, telefone, email, Nome do animal - COMPORTAMENTO: ), faça o cadastro de pets(Nome do pet, nome do tutor, idade, tamanho, peso COMPORTAMENTO:), cadastre o cuidador(nome, endereço, telefone, email, turno, especialidade COMPORTAMENTO:).
class cadastro_cliente():
    def __init__(self, nome, endereco, telefone, email, Nome_do_animal):
        self.nome = nome
        self.endereco = endereco
        self.telefone = telefone
        self.email = email
        self.Nome_do_animal = Nome_do_animal  
        # Exiba os dados do tutor

        return(f"Seus dados são nome:{nome},endereco:{endereco}, telefone:{telefone}, email:{email}, Nome do seu Pet:{Nome_do_animal}")

class cadastro_pet():
    def __init__(self,Nome_do_animal,nome_pet,nome_tutor,idade,tamanho,peso,comportamento):
        self.Nome_do_animal = Nome_do_animal
        self.nome_pet = nome_pet
        self.nome_tutor = nome_tutor
        self.idade = idade
        self.tamanho = tamanho
        self.peso = peso
        self.comportamento = comportamento
                 # Exiba os dados do Pet   
        print(f"Seus dados do seu Pet, Animal:{Nome_do_animal},Nome do seu Pet:{nome_pet}, nome do tutor:{nome_tutor}, idade:{idade}, tamanho:{tamanho}, peso:{peso}, comportamento:{comportamento}")
    def acao(self):
            # Se o Pet for cachorro ele deve latir
            if self.Nome_do_animal == "cachorro":
                return "Au Au"
            # Se o Pet for gato deve miar
            elif self.Nome_do_animal == "gato":
                return "Miau"
            # Se o Pet for pássaro deve voar
            elif self.Nome_do_animal == "passaro":
                return "Esta voando"

class cadastro_tutor():
    def __init__(self, nome, endereco, telefone, email, Nome_do_animal,comportamento,turno, especialidade ):
        self.nome = nome
        self.endereco = endereco
        self.telefone = telefone
        self.email = email
        self.Nome_do_animal = Nome_do_animal
        self.comportamento = comportamento
        self.turno = turno
        self.especialidade = especialidade
        # Exiba os dados do cuidador 
        print(print(f"Seus dados do seu tutor, nome:{nome},endereco:{endereco}, telefone:{telefone}, email:{email}, Nome do animal que esta cuidando:{Nome_do_animal}, comportamento:{comportamento}, turno:{turno},especialidade:{especialidade}"))

cao = cadastro_pet("cachorro","dalei","carlos",6,"70 cm","55 kg","docil")
print(cao.acao())
