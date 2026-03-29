import pandas as pd
import numpy as np

#EXERCICIO1 ->  Carregar o dataset
df = pd.read_csv('paises.csv', delimiter=';')

# a. Filtrando países que contêm 'OCEANIA' na região
oceania_countries = df[df['Region'].str.contains('OCEANIA', case=False, na=False)]
print("Países da Oceania:")
print(oceania_countries['Country'])

# b. Contando a quantidade de países na Oceania
count_oceania = len(oceania_countries)
print(f"\nTotal de países na Oceania: {count_oceania}\n")

# idxmax() retorna o ÍNDICE (label) da linha onde o valor é máximo
# Usar índice com loc[] para pegar toda a linha do país
idx_maior_pop = df['Population'].idxmax()
pais_maior_pop = df.loc[idx_maior_pop]
print("EXERCÍCIO 2 | País com maior população |")
print(f"  Nome:   {pais_maior_pop['Country']}")
print(f"  Região: {pais_maior_pop['Region']}")
print(f"  Pop.:   {pais_maior_pop['Population']:,}")
 
df['Literacy (%)'] = df['Literacy (%)'].astype(str).str.replace(',', '.').astype(float)
# --- SITUAÇÃO A: MÉDIA POR REGIÃO CONSIDERANDO O ZERO COMO VALOR REAL ---
# Groupby diretamente no dataset original.
media_com_zeros = df.groupby('Region')['Literacy (%)'].mean()

# --- SITUAÇÃO B: MÉDIA POR REGIÃO CONSIDERANDO O ZERO COMO VALOR FALTANTE (NaN) ---
# O Pandas, por padrão, ignora valores NaN ao calcular a média (.mean()).
df_tratado = df.copy()
df_tratado['Literacy (%)'] = df_tratado['Literacy (%)'].replace(0, np.nan)

# Calcular a média agrupada novamente
media_sem_zeros = df_tratado.groupby('Region')['Literacy (%)'].mean()

# DataFrame comparativo (que você já criou)
comparativo = pd.DataFrame({
    'Média (Com Zeros)': media_com_zeros,
    'Média (S/ Zeros-NaN)': media_sem_zeros
})

#adicionando uma coluna 'Diferença' atribuindo o resultado da subtração
comparativo['Diferença'] = comparativo['Média (S/ Zeros-NaN)'] - comparativo['Média (Com Zeros)']

#Ordenar pela diferença ajuda a ver onde o impacto do NaN foi maior
comparativo = comparativo.sort_values(by='Diferença', ascending=False)

print("\nEXERCÍCIO 3 | Comparativo de Alfabetização por Região (Atualizado) |\n")
print(comparativo)

# Exemplo de interpretação do resultado:
print("\nNota:")
print("Regiões como 'WESTERN EUROPE', a média sobe de ~80% para ~98% ")
print("quando tratamos o zero '0' como informação faltante (NaN).\n")

# Filtrando países com Coastline igual a 0
no_coast = df[df['Coastline (coast/area ratio)'] == 0]

# Selecionando apenas os nomes dos países
no_coast_names = no_coast['Country']

# Salvando em um novo arquivo CSV
no_coast_names.to_csv('noCoast.csv', index=False)
print("EXERCICIO 4 | Arquivo 'noCoast.csv' gerado com sucesso |\n")

# Limpeza para Garantir que Deathrate seja numérico
# Trocar a vírgula por ponto (se houver) e transformar em float
df['Deathrate'] = df['Deathrate'].astype(str).str.replace(',', '.').astype(float)

# Definir a função conforme o enunciado < 9
def humanitarian_check(rate):
    if rate < 9:
        return 'Balanced'
    else:
        return 'Urgent'

# NSERIR nova coluna aplicando a função na coluna Deathrate
df['Humanitarian Help'] = df['Deathrate'].apply(humanitarian_check)
# Mostrando as colunas específicas para conferir
print("Exercicio 5 | Dataset com a nova coluna 'Humanitarian Help' |")
print(df[['Country', 'Deathrate', 'Humanitarian Help']].head(20))

#Resumo para bater com os seus números)
resumo = df['Humanitarian Help'].value_counts()
print("\nResumo da classificação:")
print(resumo)

#Salvar o dataset original e atualiza-lo
df.to_csv('paises.csv', sep=';', index=False)
print("Dataset original atualizado com a inserção da nova coluna 'Humanitarian Help'\n")

#Boa p´ratica criar um nome diferente para o dataset que foi atualizado, não alterar o original
#df.to_csv('paises_atualizado.csv', sep=';', index=False)
