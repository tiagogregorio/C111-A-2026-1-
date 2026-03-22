import pandas as pd
import numpy as np

#Questão 1 - Criar Series
seriesAno1 = pd.Series({'Java': 16.25, 'C': 16.04, 'Python': 9.85})
seriesAno2 = pd.Series({'C': 16.21, 'Python': 12.12, 'Java': 11.68})
print("Questão1")
print(seriesAno1)
print(seriesAno2)

#Questão 2 - Porcentagem total que representam no mercado
print("\nQuestão2")
print(f"Total Ano 1: {seriesAno1.sum()}%") 
print(f"Total Ano 2: {seriesAno2.sum()}%")

# Questão 3 - Crescimento/Declínio 
# O Pandas alinha automaticamente as labels antes de subtrair 
variacao = seriesAno2 - seriesAno1
print("\nQuestão3")
print("Variação de mercado:")
print(variacao)

# Questão 4 - Apenas linguagens que tiveram crescimento 
crescimento = variacao[variacao > 0] #pensar em uma reta, movimento lado direito
print("\nQuestão4")
print("Linguagens que cresceram:")
print(crescimento)

# Questão 5 - Projeção para daqui a 2 anos 
# Lógica: Valor Atual + (Variação * 2 anos)
projecao = seriesAno2.add(variacao * 2, fill_value=0)
# nlargest(1) retorna o maior valor e sua label rapidamente 
print("\nQuestão5")
print(f"Linguagem mais popular em 2 anos: {projecao.nlargest(1)}")

#Questão 6 - Dataframe exmplo do tópico 5.3
print("\nQuestão6")
# Define seed para repetir valores
np.random.seed(10)
df = pd.DataFrame(
    index=['A', 'B', 'C', 'D', 'E'],
    columns=['W', 'X', 'Y', 'Z'],
    data=np.random.randint(1, 50, [5, 4])
)
# Seleciona coluna X
coluna_x = df['X']
# Filtra valores menores que 30
filtro = coluna_x < 30
# Calcula média
media = coluna_x[filtro].mean()
print("Média dos elementos da coluna X que são menores que 30:", media)

#Questão 7 média dos elementos da linha D usando a função loc() como base e a soma 
# dos elementos da linha E usando a função iloc() como base
print("\nQuestão7")
media_linha_d = df.loc['D'].mean()
soma_linha_e = df.iloc[4].sum() 
print(f"Média Linha D: {media_linha_d} | Soma Linha E: {soma_linha_e}")

# Questão 8 - Slicing
print("\nQuestão8")
df_fatiado = df.loc[['A', 'C', 'E'], ['X', 'Y']]
print("DataFrame Fatiado (A, C, E | X, Y):")
print(df_fatiado)
print("\nSoma das Linhas:")
print(df_fatiado.sum(axis=1)) # axis=1 para somar horizontalmente (Linha)
print("\nSoma das Colunas:")
print(df_fatiado.sum(axis=0)) # axis=0 para somar verticalmente 
