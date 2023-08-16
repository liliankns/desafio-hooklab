import pandas as pd
import matplotlib.pyplot as plt

# Exploração dos Dados
dados = pd.read_json("dados_compras.json")

valores_ausentes_coluna = dados.isna().sum()

print(f"{dados}\n")

print("Número de valores ausentes por coluna:")
print(f"{valores_ausentes_coluna}\n")

qtd_compras = len(dados)
print(f"Quantidade total de compras realizadas: {qtd_compras}")

# Análise de Compras
soma_valores_compras = dados['Valor'].sum()
media_valores_compras = soma_valores_compras / qtd_compras
print(f"Média dos gastos das compras: {media_valores_compras:.2f}")

valor_minimo_compra = dados['Valor'].min()
print(f"Valor mínimo gasto por compra: {valor_minimo_compra}")

valor_maximo_compra = dados['Valor'].max()
print(f"Valor máximo gasto por compra: {valor_maximo_compra}")

index_valor_maximo = dados['Valor'].idxmax()
produto_valor_maximo = dados.loc[index_valor_maximo, 'Nome do Item']
print(f"Produto mais caro: {produto_valor_maximo}")

index_valor_minimo = dados['Valor'].idxmin()
produto_valor_minimo = dados.loc[index_valor_minimo, 'Nome do Item']
print(f"Produto mais barato: {produto_valor_minimo}\n")

# Segmentação por Gênero
print("Distribuição de gênero:")
contagem_sexo = dados['Sexo'].value_counts()
print(f"{contagem_sexo}\n")

print("Gasto em compras por gênero:")
valor_gasto_genero = dados.groupby('Sexo')['Valor'].sum()
print(f"{valor_gasto_genero}\n")

# Visualização de Dados
total_por_genero = dados.groupby('Sexo')['Valor'].sum()
plt.figure(figsize=(8, 6))
total_por_genero.plot(kind='bar', color=['pink', 'green', 'purple'])
plt.title('Valor total gasto em compras por gênero')
plt.xlabel('')
plt.ylabel('Valor Total')
plt.xticks(rotation=0)
plt.show()

categorias = ['18-25', '26-35', '36-45', '46+']
dados['Categoria Idade'] = pd.cut(dados['Idade'], bins=[18, 25, 35, 45, float('inf')], labels=categorias)
contagem_categorias = dados['Categoria Idade'].value_counts()
plt.figure(figsize=(8, 8))
plt.pie(contagem_categorias, labels=contagem_categorias.index, autopct='%1.1f%%')
plt.title('Distribuição das idades em categorias')
plt.axis('equal')
plt.show()

contagem_itens = dados['Nome do Item'].value_counts()
top_10_itens = contagem_itens.head(10)
plt.figure(figsize=(10, 6))
top_10_itens.sort_values().plot(kind='bar', color='green')
plt.title('Top 10 itens mais comprados')
plt.xlabel('Nome do Item')
plt.ylabel('Quantidade de Compras')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()