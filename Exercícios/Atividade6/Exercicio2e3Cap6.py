import pandas as pd
import matplotlib.pyplot as plt

df_space = pd.read_csv('space.csv', delimiter=';')

#Criando uma figura que conterá 1 linha e 2 colunas de gráficos
# figsize define a largura (15) e a altura (7) total do conjunto
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 7))

#EXERCÍCIO 2 (Lado Esquerdo - ax1)
# Filtrando lançamentos realizados nos EUA e China
df_usa = df_space[df_space['Location'].str.contains('USA')]
df_china = df_space[df_space['Location'].str.contains('China')]

# Obtendo apenas empresas ÚNICAS em cada país (evitando duplicatas)
empresas_usa = df_usa['Company Name'].drop_duplicates()
empresas_china = df_china['Company Name'].drop_duplicates()

#Calculando a quantidade total de empresas únicas
qtd_usa = len(empresas_usa)
qtd_china = len(empresas_china)

# Definindo rótulos e valores para o gráfico de barras
paises_eixo = ['EUA', 'CHINA']
quantidades = [qtd_usa, qtd_china]

#Desenhando o gráfico de barras no primeiro eixo (ax1)
ax1.bar(paises_eixo, quantidades, color=['green', 'steelblue'], width=0.5)

#Adicionando os valores numéricos acima de cada barra no ax1
for i, valor in enumerate(quantidades):
    ax1.text(i, valor + 0.2, str(valor), ha='center', va='bottom', fontsize=12, fontweight='bold')

#Formatar títulos e legendas do ax1
ax1.set_title('Número de Empresas Espaciais\nEUA vs China', fontsize=14, fontweight='bold')
ax1.set_xlabel('Países', fontsize=12)
ax1.set_ylabel('Quantidade de Empresas', fontsize=12)
ax1.set_ylim(0, max(quantidades) + 3) # Define margem superior para o texto não ser cortado (superior)

##############################################
#EXERCÍCIO 3 (Lado Direito - ax2)
# Filtrando missões apenas da empresa 'Roscosmos'
df_roscosmos = df_space[df_space['Company Name'] == 'Roscosmos']

# Contando missões com Sucesso e missões com Falha (qualquer status != Success)
missoes_sucesso = len(df_roscosmos[df_roscosmos['Status Mission'] == 'Success'])
missoes_falha = len(df_roscosmos[df_roscosmos['Status Mission'] != 'Success'])

#Preparando dados para o gráfico de torta
valores_torta = [missoes_sucesso, missoes_falha]
rotulos_torta = ['Sucesso', 'Falha']
cores_torta = ['mediumseagreen', 'red']
explode_torta = (0, 0.15) # Destaca a fatia de falha (afastando-a do centro)

#Desenhando o gráfico de torta no segundo eixo (ax2)
ax2.pie(valores_torta, labels=rotulos_torta, autopct='%1.2f%%', colors=cores_torta, 
        explode=explode_torta, startangle=140, textprops={'fontsize': 11})

#Adicionando título ao gráfico de torta no ax2
ax2.set_title('Missões da Roscosmos-Cazaquistão\n(Operado pela Rússia)\nSucesso vs Falha', fontsize=14, fontweight='bold')

#Ajustando o layout para que os gráficos não fiquem sobrepostos e mostrar
plt.tight_layout()
#(Opcional) Salvar a imagem em png
plt.savefig('exercicios_espaciais_combinados.png', dpi=150)
plt.show()

