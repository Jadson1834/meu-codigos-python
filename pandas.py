# Desafio: A partir do modelo, crie uma tabela de uma escola com: Nome, Turma, Idade, Curso e Situação
import pandas as pd

# Criando um DataFrame a partir de um dicionário
escola = {'Nome': ['Carlos', 'Marcos', 'Dane', 'David'],
         'Turma':['INF03','INF08','INF09','INF06'],
         'Idade': [20, 19, 15, 23],
         'Curso': ['TI', 'Radiologia', 'Enfermagem', 'Administração'],
         'Situação':['Boa','Vulnerabilidade Social','Excelente','Ruim'],
         'Notas':[5,7,9,5]}

df = pd.DataFrame(escola)

# exibindo alunos aprovados e tem mais de 18
for index,row in df.iterrows():
        if row['Notas'] >= 7 and row['Idade'] > 18:
            print(f"parabens {row['Nome']} sua nota foi: {row['Notas']}, Aprovado")
# criando um arquivo CSV
df.to_csv('boletim.csv', index=False)
