import pandas as pd
import matplotlib.pyplot as plt

# EXERCÍCIO 1 - Gráfico de Linhas: Deathrate e Birthrate dos países da América do Norte (dataset paises.csv)
df_paises = pd.read_csv('paises.csv', delimiter=';')

# Filtrando apenas os países da região 'NORTHERN AMERICA'
# str.strip() remove espaços em branco extras ao redor do nome da região e ordenar para facilidar leitura
df_norte = df_paises[df_paises['Region'].str.strip() == 'NORTHERN AMERICA']
df_norte = df_norte.sort_values(by='Birthrate', ascending=True) # do menor para maior

# Extraindo a coluna com os nomes dos países (eixo X dos gráficos)
paises = df_norte['Country'].str.strip()

# Extraindo a taxa de mortalidade (Deathrate) e a taxa de natalidade (Birthrate) de cada país
deathrate = df_norte['Deathrate']
birthrate = df_norte['Birthrate']

# Criando a figura com tamanho legal para exibir o gráfico
plt.figure(figsize=(10, 5))

# - 'o--r' → marcador circular, linha tracejada, cor vermelha (Deathrate)
# - 's-g'  → marcador quadrado, linha sólida, cor verde (Birthrate)
plt.plot(paises, birthrate, 's-g',  label='Taxa de Natalidade (Birthrate)',  linewidth=2, markersize=8)
plt.plot(paises, deathrate, 'o--r', label='Taxa de Mortalidade (Deathrate)', linewidth=2, markersize=8)

# Adicionando título descritivo ao gráfico e adicionando rotulo no eixos x e y
plt.title('Taxa de Mortalidade e Natalidade\nPaíses da América do Norte', fontsize=14, fontweight='bold')
plt.xlabel('Países ordenado por natalidade', fontsize=11)
#coloquei Taxa por 1000 habitantes, porque é uma convenção demográfica da (CIA World Factbook)
plt.ylabel('Taxa (por 1000 habitantes)', fontsize=11)

# Rotacionando os nomes dos países no eixo X para um visual melhor
plt.xticks(rotation=25, ha='right', fontsize=10)

# Exibindo a legenda, adicionar grade, ajustar layout, mostrar grágico
plt.legend(fontsize=10)
plt.grid(True, linestyle='--', alpha=0.5)
plt.tight_layout()
# Salvar o gráfico gerado como arquivo PNG
plt.savefig('exercicio1_linhas.png', dpi=150)
plt.show()


