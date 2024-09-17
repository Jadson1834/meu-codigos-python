# Importar dados
import pandas as pd
import matplotlib.pyplot as plt
tabela = pd.read_csv('vendas.csv')

# Carregue os dados do arquivo vendas.csv em um DataFrame.
df = pd.DataFrame(tabela)

# Calcule a média de vendas por categoria de produto.
plt.pie(df['Vendas'], labels=df['Categoria'], autopct='%1.1f%%', startangle=140)
plt.axis('equal')
plt.title('média de vendas por categoria')
plt.show()

# Determine o produto com o maior valor de vendas totais.
plt.figure(figsize=(12,5))
plt.bar(df['Produto'], df['Vendas'])
plt.xlabel('Produto')
plt.ylabel("Vendas")
plt.grid(True)
plt.show()
# Identifique a data com a maior venda total.
plt.plot(df['Data'], df['Vendas'], marker='o', label='Vendas', color='blue', linestyle='--')

plt.xlabel('Data')
plt.ylabel('Vendas')
plt.xticks(rotation=90)
plt.legend()
plt.grid(True, which='both', linestyle='--', linewidth=0.5)
plt.tight_layout()
plt.show()
# Filtragem e Agrupamento:

# Crie um novo DataFrame filtrando apenas as vendas de produtos da categoria "Eletrônicos".
novo_df = df.groupby(['Categoria'])['Vendas'].sum()
novo_df = novo_df.drop("Gamer")
novo_df = novo_df.drop("Periféricos")
print(novo_df)
# Agrupe os dados por produto e calcule o total de vendas e a média de descontos para cada produto.
df_final = df.groupby(['Produto',"Desconto"])['Vendas'].sum()
print(df_final)
# Visualização (Opcional):

# Use o Matplotlib ou Seaborn para criar um gráfico de barras que mostre as vendas totais por categoria de produto.
